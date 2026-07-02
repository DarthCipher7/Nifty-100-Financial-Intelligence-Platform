# Nifty 100 Financial Intelligence Platform

A production-grade financial analytics platform that transforms raw financial statement data of 92 Nifty 100 companies into structured investment intelligence using ETL pipelines, data validation, SQL analytics, and dashboards.

---

## Project Overview

This project is designed to analyze Nifty 100 companies using:

- Profit & Loss statements
- Balance Sheets
- Cash Flow statements
- Stock Prices
- Market Cap data
- Financial Ratios
- Sector classification

The platform enables:
- Financial KPI computation
- Investment screening
- Sector analysis
- Peer comparison
- Financial health scoring
- Interactive dashboards

---

## Tech Stack

- Python
- Pandas
- SQLite
- SQL
- Streamlit
- Plotly
- Git & GitHub

---

## Project Architecture

```text
Raw Excel Files
      ↓
ETL Pipeline
      ↓
Data Validation
      ↓
SQLite Database
      ↓
Analytics Engine
      ↓
Dashboard / Reports
```

---

## Sprint Progress

### Sprint 1 — Foundation & ETL ✅

Completed:
- Project setup
- Excel loader engine
- Data inspection
- Normalization engine
- Validation rules
- Data cleaning pipeline
- SQLite database creation

Modules built:
- loader.py
- normalizer.py
- validator.py
- database.py

---

## Folder Structure

```text
NIFTY100/
│
├── src/
│   └── etl/
├── tests/
├── data/
├── db/
├── output/
```

---

## Author

**Aashaan Gaigole**