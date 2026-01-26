# Portfolio Optimization - GMF Investments

## Overview
This project implements time series forecasting and portfolio optimization strategies for Guide Me in Finance (GMF) Investments. The project analyzes historical financial data for three key assets (TSLA, BND, SPY) to enhance portfolio management strategies through predictive modeling and risk analysis.

## Project Structure
```
portfolio-optimization/
├── .vscode/              # VS Code settings
├── .github/workflows/    # CI/CD workflows
├── data/                 # Data directory
│   └── processed/        # Processed data files
├── notebooks/            # Jupyter notebooks for analysis
├── src/                  # Source code
├── tests/                # Unit tests
├── scripts/              # Utility scripts
├── requirements.txt      # Project dependencies
└── README.md            # This file
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd portfolio-optimization
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Assets Analyzed

| Asset | Ticker | Description | Risk Profile |
|-------|--------|-------------|--------------|
| Tesla | TSLA | High-growth stock in consumer discretionary sector | High risk, high potential return |
| Vanguard Total Bond Market ETF | BND | Tracks U.S. investment-grade bonds | Low risk, stability and income |
| S&P 500 ETF | SPY | Tracks the S&P 500 Index | Moderate risk, broad market exposure |

## Business Objective

**Guide Me in Finance (GMF) Investments** is a forward-thinking financial advisory firm specializing in personalized portfolio management. This project leverages cutting-edge technology and data-driven insights to provide tailored investment strategies through advanced time series forecasting models.

### Goals
- Predict market trends using historical financial data
- Optimize asset allocation for client portfolios
- Enhance portfolio performance by minimizing risks
- Capitalize on market opportunities through data-driven insights

## Project Tasks

### Task 1: Data Preprocessing and Exploration ✅

**Objective:** Load, clean, and understand historical financial data to prepare it for modeling.

**What's Included:**
- ✓ Data extraction from YFinance (TSLA, BND, SPY)
- ✓ Data cleaning and quality assessment
- ✓ Exploratory Data Analysis (EDA) with visualizations
- ✓ Stationarity testing (Augmented Dickey-Fuller test)
- ✓ Risk metrics calculation (VaR, Sharpe Ratio)
- ✓ Correlation analysis between assets
- ✓ Outlier detection and volatility analysis

**Deliverables:**
- `notebooks/task1_data_exploration.ipynb` - Complete EDA notebook
- `data/processed/` - Cleaned and processed data files
- Multiple insightful visualizations
- Comprehensive statistical analysis

## Usage

### Quick Start - Data Extraction

```bash
# Run the data extraction script
python scripts/extract_data.py
```

### Task 1: Data Preprocessing and Exploration

1. Navigate to the notebooks directory:
```bash
cd notebooks
```

2. Launch Jupyter Lab:
```bash
jupyter lab
```

3. Open `task1_data_exploration.ipynb`

4. Run all cells to:
   - Extract historical financial data using YFinance
   - Perform data cleaning and exploratory analysis
   - Conduct stationarity tests (ADF)
   - Calculate risk metrics (VaR, Sharpe Ratio)
   - Generate comprehensive visualizations
   - Save processed data for modeling

## Testing

Run tests using pytest:
```bash
pytest tests/ -v
```

## Contributing

TBD

## License

TBD
