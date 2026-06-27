# Pakistan Stock Exchange (PSX) Market Intelligence Engine

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL" />
  <img src="https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black" alt="Power BI" />
  <img src="https://img.shields.io/badge/Linux%20/%20Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white" alt="Ubuntu" />
  <img src="https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white" alt="VS Code" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
</p>

## 📌 Project Overview
In fast-moving equity markets like the Pakistan Stock Exchange (PSX), portfolio managers, risk officers, and retail desks require rapid, data-driven insights to capture alpha and mitigate risk. Raw trading data is often fragmented, dense, and difficult to parse for macro trends or individual ticker anomalies.

**The Solution:** This project delivers a production-grade, end-to-end BI pipeline that ingests **9 years of historical PSX data** (spanning 2017 to 2025). The system cleanses trading noise, structures the data into an optimized analytical relational schema, and delivers interactive dashboards highlighting liquidity trends, market volatility, and top-performing sectors or equities.

---

## 🛠️ Tech Stack & Architecture
* **Developer:** Dawood Raza
* **Role:** Business Intelligence Analyst / Data Engineer
* **Target Architecture:** Python (ETL) ➔ SQL Relational DB ➔ Power BI Semantic Model

### Data Pipeline Flow
```text
[Raw CSV: compiled_psx_historical_2017_2025.csv]
                        │
                        ▼
          [Python ETL & Cleaning Script]
                        │
                        ▼
       [Structured Database / SQL Warehouse] 
                        │
                        ▼
       [Power BI / Semantic Modeling (DAX)] 
                        │
                        ▼
   [Executive Dashboard & Actionable Insights]
