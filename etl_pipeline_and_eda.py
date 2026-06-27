# ==============================================================================
# PSX HISTORICAL DATA CLEANING & ETL PIPELINE (2017-2025)
# Designed for: Pakistan Stock Exchange Historical Analysis
# Data Engineer: Dawood Raza
# ==============================================================================

import os
import numpy as np
import pandas as pd

# ------------------------------------------------------------------------------
# STEP 1: DEFINE PATHS AND EXTRACT DATA INTO MEMORY
# ------------------------------------------------------------------------------
print("Executing Step 1: Loading raw PSX historical data...")
base_dir = "/home/dawood-raza/Desktop/New Folder"
file_path = os.path.join(base_dir, "compiled_psx_historical_2017_2025.csv")

# Load dataset into memory
df = pd.read_csv(file_path)
print(f"-> Raw Dataset Shape Loaded: {df.shape}")

# ------------------------------------------------------------------------------
# STEP 2: AUDIT CHRONOLOGY (TIMELINE INTEGRITY)
# ------------------------------------------------------------------------------
print("\nExecuting Step 2: Converting dates and auditing timeline...")
df["DATE"] = pd.to_datetime(df["DATE"], errors="coerce")

print(f"-> Historical Start Date: {df['DATE'].min()}")
print(f"-> Historical End Date:   {df['DATE'].max()}")
print(f"-> Missing Date Records:  {df['DATE'].isnull().sum()}")

# ------------------------------------------------------------------------------
# STEP 3: DATA ENGINEERING - FORWARD FILL ZERO VALUES
# ------------------------------------------------------------------------------
print(
    "\nExecuting Step 3: Applying Time-Series Forward-Fill on non-trading days..."
)

# DESIGN NOTE: WHY WE CANNOT LEAVE 0.0 IN THE FILE:
# If a stock doesn't trade on a day, the raw feed records OPEN/HIGH/LOW as 0.0.
# If left as zero, any average calculations (e.g., Average Open Price) in SQL/Power BI
# pull down heavily toward zero, ruining line charts and performance analysis.

# DESIGN NOTE: WHY WE USE THE LAST TRADED DAY VALUE (FORWARD FILL):
# Real-world assets don't lose all value when no one trades them. The value remains
# flat, exactly what it was on the last active trading day. Carrying forward the
# previous valid day's closing price maintains realistic horizontal trendlines.

# Sort sequentially by company ticker and trading date
df = df.sort_values(by=["SYMBOL", "DATE"]).reset_index(drop=True)

# Replace fake 0.0 values with NaN so pandas can see them
for col in ["OPEN", "HIGH", "LOW"]:
    df[col] = df[col].replace(0.0, np.nan)

# Forward fill prices group by company ticker so prices don't blend between different symbols
df[["OPEN", "HIGH", "LOW"]] = df.groupby("SYMBOL")[
    ["OPEN", "HIGH", "LOW"]
].ffill()

# For rows at the absolute beginning of history with no previous day, fallback to current CLOSE
df["OPEN"] = df["OPEN"].fillna(df["CLOSE"])
df["HIGH"] = df["HIGH"].fillna(df["CLOSE"])
df["LOW"] = df["LOW"].fillna(df["CLOSE"])

# ------------------------------------------------------------------------------
# STEP 4: CORRECT REMAINING LOGIC/BOUNDARY VIOLATIONS (31,985 ROWS)
# ------------------------------------------------------------------------------
print("\nExecuting Step 4: Correcting cross-field intraday logic violations...")

# Target rows where intraday flow fails logic (e.g., recorded LOW is higher than HIGH)
bad_rows_mask = (
    (df["HIGH"] < df["OPEN"])
    | (df["HIGH"] < df["CLOSE"])
    | (df["LOW"] > df["OPEN"])
    | (df["LOW"] > df["CLOSE"])
    | (df["LOW"] > df["HIGH"])
)

# Overwrite broken boundaries by safely pinning them to the verified CLOSE price
df.loc[bad_rows_mask, "OPEN"] = df.loc[bad_rows_mask, "CLOSE"]
df.loc[bad_rows_mask, "HIGH"] = df.loc[bad_rows_mask, "CLOSE"]
df.loc[bad_rows_mask, "LOW"] = df.loc[bad_rows_mask, "CLOSE"]

# ------------------------------------------------------------------------------
# STEP 5: ELIMINATE ABSOLUTE ZERO/NEGATIVE PRICE ANOMALIES (3,866 ROWS)
# ------------------------------------------------------------------------------
print("\nExecuting Step 5: Dropping absolute zero and negative price anomalies...")

# Drop the remaining dead rows where prices are less than or equal to 0
df = df[
    (df["CLOSE"] > 0) & (df["OPEN"] > 0) & (df["HIGH"] > 0) & (df["LOW"] > 0)
]

# ------------------------------------------------------------------------------
# STEP 6: DATA METRICS COMPLIANCE CHECK
# ------------------------------------------------------------------------------
print("\nExecuting Step 6: Database Compliance Summary Verification:")

final_logic_errors = df[
    (df["HIGH"] < df["OPEN"])
    | (df["HIGH"] < df["CLOSE"])
    | (df["LOW"] > df["OPEN"])
    | (df["LOW"] > df["CLOSE"])
    | (df["LOW"] > df["HIGH"])
]
final_price_errors = df[
    (df["CLOSE"] <= 0) | (df["OPEN"] <= 0) | (df["HIGH"] <= 0) | (df["LOW"] <= 0)
]

print(f"-> Final Intraday Logic Errors remaining: {len(final_logic_errors)}")
print(f"-> Final Zero/Negative Price Anomalies:   {len(final_price_errors)}")
print(f"-> Total Unique Trading Tickers Kept:     {df['SYMBOL'].nunique()}")

# ------------------------------------------------------------------------------
# STEP 7: EXPORT PRISTINE PRODUCTION-READY DATASET
# ------------------------------------------------------------------------------
print("\nExecuting Step 7: Saving immaculate dataset back to Desktop...")
output_file = os.path.join(base_dir, "cleaned_psx_historical_2017_2025.csv")
df.to_csv(output_file, index=False)

print(f"\nSUCCESS! 🚀 Pristine pipeline file exported perfectly to:\n{output_file}")
