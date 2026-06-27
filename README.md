# 📈 Institutional PSX Equity Research & Analytics Pipeline (2017 - 2025)
[![Data Pipeline](https://img.shields.io/badge/Pipeline-Python%20%E2%9E%94%20Parquet%20%E2%9E%94%20PowerBI-blue.svg)](#)
[![Data Engine](https://img.shields.io/badge/Engine-Pandas%20%7C%20PyArrow-emerald.svg)](#)
[![Domain](https://img.shields.io/badge/Domain-Institutional%20Equity%20Research-gold.svg)](#)

## 1. Executive Summary & Business Case
In high-velocity equity markets like the Pakistan Stock Exchange (PSX), portfolio managers, risk desks, and investment analysts face a massive operational hurdle: parsing through vast, uncompressed, multi-year daily transaction logs to isolate macro-level sectoral liquidity and specific equity performance metrics.

**The Solution:** This project establishes a production-grade analytics lifecycle. It transforms 9 years of historical market raw data (`compiled_psx_historical_2017_2025.csv`) into a decoupled star-schema architecture. By migrating heavy computations upstream to a custom Python ETL pipeline, the dataset's local memory footprint was reduced by over **80%**, empowering standard local machines to execute sub-second data refreshes and run lightning-fast visual cross-filtering inside an elite, Bloomberg-terminal-inspired Power BI dashboard.

---

## 2. Interface Preview (Production Analytics)

To maximize data visibility and replicate an institutional environment, the user interface features a high-density, low-glare dark design language optimized for real-time risk assessment and asset monitoring.

<kbd>
  <img src="docs/dashboard_preview.png" alt="Executive Market Analytics Interface" width="100%">
</kbd>

*Figure 1.0: Consolidated Micro-Screener and Sector Asset Allocator View inside Power BI.*

---

## 3. Technical Workflow Architecture

The pipeline splits computational load from the presentation layer to protect analytical performance:
