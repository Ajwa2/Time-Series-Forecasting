# Data Directory

This directory contains all data files for the GMF Investments Portfolio Optimization project.

## Structure

- `processed/`: Cleaned and processed data ready for modeling

## Data Sources

All data is sourced from **YFinance** (Yahoo Finance) API covering the period from **January 1, 2015** to **January 15, 2026**.

## Assets

### TSLA (Tesla, Inc.)
- **Type:** Stock
- **Sector:** Consumer Discretionary (Automobile Manufacturing)
- **Risk Profile:** High risk, high potential return
- **Use Case:** Growth component of portfolio

### BND (Vanguard Total Bond Market ETF)
- **Type:** Bond ETF
- **Tracks:** U.S. investment-grade bonds
- **Risk Profile:** Low risk, stability and income
- **Use Case:** Defensive/stability component of portfolio

### SPY (SPDR S&P 500 ETF Trust)
- **Type:** Equity ETF
- **Tracks:** S&P 500 Index
- **Risk Profile:** Moderate risk, broad market exposure
- **Use Case:** Market benchmark and diversified equity exposure

## Data Fields

Each dataset includes:
- **Date:** Trading day timestamp (index)
- **Open:** Opening price for the day
- **High:** Highest price during the day
- **Low:** Lowest price during the day
- **Close:** Closing price for the day
- **Adj Close:** Adjusted close price (accounts for dividends and splits)
- **Volume:** Total number of shares/units traded
- **Daily_Return:** Calculated daily percentage change (added during processing)

## Processed Data Files

After running Task 1 notebook, the following files will be generated in `processed/`:

- `TSLA_processed.csv`: Tesla stock data with daily returns
- `BND_processed.csv`: Bond ETF data with daily returns
- `SPY_processed.csv`: S&P 500 ETF data with daily returns
- `all_returns.csv`: Combined daily returns for all assets
- `summary_statistics.csv`: Comprehensive statistics for all assets

## Usage

```python
import pandas as pd

# Load processed data
tsla = pd.read_csv('data/processed/TSLA_processed.csv', index_col=0, parse_dates=True)
bnd = pd.read_csv('data/processed/BND_processed.csv', index_col=0, parse_dates=True)
spy = pd.read_csv('data/processed/SPY_processed.csv', index_col=0, parse_dates=True)

# Load combined returns
returns = pd.read_csv('data/processed/all_returns.csv', index_col=0, parse_dates=True)
```
