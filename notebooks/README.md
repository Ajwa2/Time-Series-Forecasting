# Notebooks

This directory contains Jupyter notebooks for exploratory data analysis, model development, and visualization.

## Notebooks

### Task 1: Data Exploration (`task1_data_exploration.ipynb`) ✅
**Objective:** Load, clean, and understand historical financial data

**Contents:**
1. Data extraction from YFinance (TSLA, BND, SPY)
2. Data cleaning and quality checks
3. Exploratory Data Analysis (EDA)
   - Price trends over time
   - Daily returns analysis
   - Rolling statistics (volatility)
   - Distribution analysis
   - Outlier detection
4. Stationarity testing (ADF tests)
5. Risk metrics calculation (VaR, Sharpe Ratio)
6. Correlation analysis
7. Summary statistics

**Outputs:**
- Processed data files in `../data/processed/`
- 10+ professional visualizations
- Statistical analysis reports

---

### Task 2: Forecasting Models (`task2_forecasting_models.ipynb`) ✅
**Objective:** Build and evaluate time series forecasting models for TSLA

**Contents:**
1. Data preparation (chronological train/test split)
2. ARIMA/SARIMA Model
   - Stationarity testing
   - ACF/PACF analysis
   - Auto ARIMA parameter selection
   - Model training and forecasting
3. LSTM Model
   - Sequence data preparation
   - Architecture design (3 LSTM layers + dropout)
   - Model training with callbacks
   - Forecast generation
4. Model Evaluation
   - Performance metrics (MAE, RMSE, MAPE)
   - Model comparison
   - Residual analysis
   - Side-by-side forecast visualization
5. Discussion and Recommendations
   - Model strengths/weaknesses
   - Performance analysis
   - Production recommendations
   - Risk management strategies

**Outputs:**
- `../data/processed/arima_model.pkl` - Trained ARIMA model
- `../data/processed/lstm_model.h5` - Trained LSTM model
- `../data/processed/lstm_scaler.pkl` - Scaler for LSTM
- `../data/processed/model_comparison.csv` - Performance metrics
- `../data/processed/model_predictions.csv` - All forecasts
- `../data/processed/model_info.json` - Model parameters

---

### Task 3: Future Forecasts (`task3_future_forecasts.ipynb`) ✅
**Objective:** Forecast future market trends using the best-performing model

**Contents:**
1. Load best model from Task 2
2. Generate 6-12 month forecasts
   - ARIMA forecasts with confidence intervals
   - LSTM multi-step forecasts
3. Visualize forecasts
   - Historical data + forecasts
   - Confidence intervals
   - Trend analysis
4. Market opportunities and risks assessment
5. Critical reliability assessment
6. Recommendations for GMF Investments

**Outputs:**
- `../data/processed/future_forecasts.csv` - Forecast data
- `../data/processed/forecast_summary.json` - Key metrics and recommendations
- Professional forecast visualizations

---

### Task 4: Portfolio Optimization (`task4_portfolio_optimization.ipynb`) ✅
**Objective:** Construct optimal portfolio using Modern Portfolio Theory

**Contents:**
1. Load historical data and forecasts
2. Prepare expected returns
   - TSLA: From forecast (Task 3)
   - BND & SPY: Historical averages
3. Compute covariance matrix
4. Generate Efficient Frontier
   - Minimum Volatility Portfolio
   - Maximum Sharpe Ratio Portfolio
5. Visualize Efficient Frontier and key portfolios
6. Portfolio recommendation with justification

**Outputs:**
- `../data/processed/portfolio_optimization.json` - Portfolio weights and metrics
- `../data/processed/portfolio_comparison.csv` - Portfolio comparison
- `../data/processed/covariance_matrix.csv` - Covariance matrix
- `../data/processed/expected_returns.csv` - Expected returns
- Efficient Frontier visualizations

---

### Task 5: Strategy Backtesting (`task5_strategy_backtesting.ipynb`) ✅
**Objective:** Validate portfolio strategy by simulating performance on historical data

**Contents:**
1. Define backtesting period (2025-2026)
2. Define benchmark portfolio (60% SPY / 40% BND)
3. Simulate strategy performance
   - Buy and hold approach
   - Monthly rebalancing (optional)
4. Calculate performance metrics
   - Total return, annualized return
   - Sharpe Ratio, volatility
   - Maximum drawdown
5. Visualize performance comparison
   - Cumulative returns plots
   - Performance metrics charts
   - Drawdown analysis
6. Strategy viability analysis and conclusion
7. Backtest limitations discussion

**Outputs:**
- `../data/processed/backtest_metrics.csv` - Performance metrics
- `../data/processed/backtest_cumulative_returns.csv` - Cumulative returns
- `../data/processed/backtest_drawdowns.csv` - Drawdown data
- `../data/processed/backtest_summary.json` - Complete backtest summary
- Comprehensive visualizations and analysis

---

## Usage

### Running the Notebooks

To start Jupyter Lab:
```bash
jupyter lab
```


Key packages:
- `yfinance` - Data extraction
- `pandas, numpy` - Data manipulation
- `matplotlib, seaborn` - Visualization
- `statsmodels, pmdarima` - ARIMA models
- `tensorflow, keras` - LSTM models
- `scikit-learn` - Preprocessing and metrics
