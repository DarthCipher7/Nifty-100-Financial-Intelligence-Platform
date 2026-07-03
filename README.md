# Nifty 100 Financial Intelligence Platform

> Production-grade financial analytics platform built to transform raw financial statement data of Nifty 100 companies into structured investment intelligence using ETL pipelines, KPI engines, SQL analytics, and interactive dashboards.

---

## Overview

The Nifty 100 Financial Intelligence Platform is a comprehensive analytics system designed to process, validate, analyze, and rank financial data across Nifty 100 companies.

The platform transforms raw financial datasets into actionable investment intelligence through:

- ETL Pipelines  
- Data Validation & Cleaning  
- Financial KPI Computation  
- Investment Screening  
- Financial Health Scoring  
- Company Ranking  
- Dashboard & Reporting  

This project simulates an industry-grade financial intelligence platform similar to Screener, Tickertape, and institutional analytics systems.

---

## Key Features

### Data Engineering
- ETL pipeline for financial datasets
- Automated normalization and cleaning
- Data validation framework
- SQLite database integration

### Financial Analytics
- Financial Ratio Engine
- 8+ KPI calculations
- ROE, ROCE, OPM, Net Margin
- Debt/Equity, EPS, Dividend Payout
- Sales Growth Analytics

### Product Intelligence
- Investment Screener
- Financial Health Scoring
- Company Ranking Engine

### Visualization (Upcoming)
- Interactive Streamlit dashboard
- Analytics visualizations
- Automated reporting

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
Financial Ratio Engine
        ↓
Investment Screener
        ↓
Health Scoring Engine
        ↓
Ranking Engine
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

## Current Database Tables

- companies
- profitandloss
- balancesheet
- cashflow
- financial_ratios
- company_rankings

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

### Sprint 2 — Financial Ratio Engine ✅
Completed:
- Financial ratio computation engine
- KPI calculations
- Anomaly filtering
- financial_ratios table creation

KPIs Built:
- ROE
- ROCE
- Debt/Equity
- OPM
- Net Margin
- EPS
- Dividend Payout
- Sales Growth

---

### Sprint 3 — Screener & Health Scoring ✅
Completed:
- Investment screener
- Financial health scoring model
- Ranking engine
- company_rankings table creation

Features Built:
- Custom stock filtering
- Weighted health scoring
- Company ranking system

---

### Upcoming Sprints
- Sprint 4 → Sector & Peer Analytics
- Sprint 5 → Dashboard & Reporting
- Sprint 6 → Testing & Final Delivery

---

## Current Folder Structure

```text
NIFTY100/
│
├── src/
│   ├── etl/
│   └── analytics/
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

Current Stage: Sprint 3 Completed  
Build Progress: 65–70%

Core backend, analytics, and product intelligence modules completed successfully.

---

## Author

### Aashaan Gaigole  
**Data Analytics**  
Building data-driven business systems.