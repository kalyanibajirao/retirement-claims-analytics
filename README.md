# retirement-claims-analytics
End-to-end retirement claims analytics project using Python, SQL Server, and Power BI.
# Retirement Claims Analytics & Performance Dashboard

## Project Overview

An end-to-end retirement claims analytics project designed to analyze claim volumes, settlement performance, pending claims, rejection patterns, repudiation trends, and operational performance.

The project uses Python for data exploration and quality validation, SQL Server for data storage and analytical views, and Power BI for interactive dashboard development.

## Tech Stack

* Python
* Pandas
* SQL Server
* T-SQL
* Power BI
* DAX
* Data Modeling
* KPI Analytics

## Project Workflow

```text
Raw Dataset
     ↓
Python Data Exploration
     ↓
Data Quality Validation
     ↓
Data Preparation
     ↓
SQL Server
     ↓
Analytical SQL Views
     ↓
Power BI Data Model
     ↓
DAX Measures
     ↓
Interactive Dashboard
```

## Key Components

### 1. Data Exploration

The Python analysis includes:

* Dataset structure exploration
* Column identification
* Data type analysis
* Missing-value analysis
* Statistical summaries
* Business field understanding

### 2. Data Quality

Data quality checks were performed to identify:

* Missing values
* Invalid values
* Negative values
* Data-type issues
* Potential inconsistencies

### 3. SQL Server

The cleaned dataset was prepared for SQL Server and organized for analytical querying.

SQL development includes:

* Database/table creation
* Data preparation
* Analytical queries
* KPI calculations
* Power BI-ready views

### 4. Power BI Dashboard

The dashboard provides interactive analysis of retirement claims performance.

### KPI Metrics

* Total Claims
* Total Claim Amount
* Paid Claims
* Pending Claims
* Claim Settlement Rate
* Amount Settlement Rate
* Pending Rate
* Rejection Rate
* Repudiation Rate

### Dashboard Visuals

* Claim Status Distribution
* Claims Trend Over Time
* Claims by Life Insurer
* Claims by Type

### Interactive Filters

* Year
* Life Insurer
* Category

## Business Analysis

The dashboard is designed to help analyze:

* Claims processing trends
* Settlement performance
* Pending claim volumes
* Rejection patterns
* Repudiation patterns
* Differences across insurers
* Differences across claim categories
* Operational performance

## Repository Structure

```text
retirement-claims-analytics/
│
├── README.md
│
├── data/
│   └── README.md
│
├── python/
│   ├── 02_explore_data.py
│   ├── 03_data_quality.py
│   └── ...
│
├── sql/
│   ├── 01_create_database.sql
│   ├── 02_create_table.sql
│   ├── 03_data_cleaning.sql
│   ├── 04_analytical_views.sql
│   └── 05_powerbi_view.sql
│
├── powerbi/
│   ├── Retirement_Claims_Dashboard.pbix
│   └── screenshots/
│
└── documentation/
    ├── data_dictionary.xlsx
    ├── database_schema.png
    └── methodology.md
```

## Project Outcome

The project demonstrates an end-to-end analytics workflow covering data exploration, data quality validation, SQL-based analytics, KPI development, data modeling, and Power BI dashboard development.

## Author

Kalyani Bajirao

Data Analyst | Data Engineering & BI Analytics

Pune, India
