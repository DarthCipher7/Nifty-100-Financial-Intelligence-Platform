# Nifty 100 Financial Intelligence Platform

> Production-grade financial analytics platform built to transform raw financial statement data of 92 Nifty 100 companies into structured investment intelligence using ETL pipelines, SQL analytics, KPI engines, and interactive dashboards.

---

## Overview

The Nifty 100 Financial Intelligence Platform is a comprehensive analytics system designed to process, validate, analyze, and visualize financial data across 92 Nifty 100 companies.

The platform transforms raw datasets into actionable investment intelligence through:

- ETL Pipelines  
- Data Validation & Cleaning  
- Financial KPI Computation  
- Investment Screening  
- Sector Analytics  
- Financial Health Scoring  
- Dashboard & Reporting  

This project simulates an industry-grade financial intelligence platform similar to Screener, Tickertape, and institutional analytics systems.

---

## Key Features

### Data Engineering
- ETL pipeline for 12 datasets
- Automated data cleaning and normalization
- Data quality validation framework
- SQLite database integration

### Financial Analytics
- 50+ Financial KPIs
- Revenue, profit & EPS growth analysis
- Ratio computation (ROE, ROCE, OPM, D/E, CAGR)
- Financial health scoring model

### Intelligence Modules
- Investment Screener
- Sector Benchmarking
- Peer Comparison
- Cash Flow Intelligence
- Trend Analytics

### Visualization
- Interactive Streamlit dashboard
- Automated PDF reports
- Excel exports

---

## Tech Stack

- Python
- Pandas
- SQL
- SQLite
- Streamlit
- Plotly
- Git & GitHub

---

## Project Architecture

```text
Raw Excel Datasets
        ↓
ETL Pipeline
        ↓
Data Validation & Cleaning
        ↓
SQLite Database
        ↓
Financial Analytics Engine
        ↓
Dashboard / Reports
```

---

## Dataset Coverage

### Core Datasets
- companies.xlsx
- profitandloss.xlsx
- balancesheet.xlsx
- cashflow.xlsx
- analysis.xlsx
- documents.xlsx
- prosandcons.xlsx

### Supporting Datasets
- sectors.xlsx
- stock_prices.xlsx
- market_cap.xlsx
- financial_ratios.xlsx
- peer_groups.xlsx

---

## Sprint Progress

### Sprint 1 — Foundation & ETL ✅

Completed:
- Project Setup
- Excel Loader Engine
- Data Inspection
- Data Normalization
- Validation Rules
- Data Cleaning Pipeline
- SQLite Database Creation

Modules Built:
- loader.py
- normalizer.py
- validator.py
- database.py

---

### Upcoming Sprints

- Sprint 2 → Financial Ratio Engine  
- Sprint 3 → Screener & Financial Health Scoring  
- Sprint 4 → Sector, Peer & Trend Analytics  
- Sprint 5 → Dashboard & Reporting  
- Sprint 6 → Testing & Final Delivery  

---

## Current Folder Structure

```text
NIFTY100/
│
├── src/
│   └── etl/
│       ├── loader.py
│       ├── normalizer.py
│       ├── validator.py
│       └── database.py
│
├── tests/
├── data/
├── db/
├── output/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Project Status

Current Stage: Sprint 1 Completed  
Build Progress: 20%  

Core ETL and database foundation completed successfully.

---

## Author

### Aashaan Gaigole
**Data Analytics**  
Building data-driven business systems.