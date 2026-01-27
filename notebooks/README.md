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
