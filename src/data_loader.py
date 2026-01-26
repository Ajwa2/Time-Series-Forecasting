"""
Data loading utilities for GMF Investments Portfolio Optimization
"""

import yfinance as yf
import pandas as pd
from typing import List, Dict, Tuple
from datetime import datetime


class FinancialDataLoader:
    """
    A class to handle loading and basic preprocessing of financial data from YFinance.
    """
    
    def __init__(self, tickers: List[str], start_date: str, end_date: str):
        """
        Initialize the data loader.
        
        Parameters:
        -----------
        tickers : List[str]
            List of ticker symbols to download
        start_date : str
            Start date in 'YYYY-MM-DD' format
        end_date : str
            End date in 'YYYY-MM-DD' format
        """
        self.tickers = tickers
        self.start_date = start_date
        self.end_date = end_date
        self.data = {}
        
    def download_data(self, verbose: bool = True) -> Dict[str, pd.DataFrame]:
        """
        Download historical data for all tickers.
        
        Parameters:
        -----------
        verbose : bool
            Whether to print progress messages
            
        Returns:
        --------
        Dict[str, pd.DataFrame]
            Dictionary with ticker symbols as keys and DataFrames as values
        """
        if verbose:
            print(f"Downloading data from {self.start_date} to {self.end_date}...")
        
        for ticker in self.tickers:
            if verbose:
                print(f"Fetching {ticker}...")
            
            self.data[ticker] = yf.download(
                ticker, 
                start=self.start_date, 
                end=self.end_date, 
                progress=False
            )
            
            if verbose:
                print(f"{ticker}: {len(self.data[ticker])} trading days")
        
        if verbose:
            print("Data extraction completed!")
        
        return self.data
    
    def add_returns(self) -> None:
        """
        Calculate and add daily returns (percentage change) to all datasets.
        """
        for ticker in self.tickers:
            if ticker in self.data:
                self.data[ticker]['Daily_Return'] = (
                    self.data[ticker]['Close'].pct_change() * 100
                )
    
    def handle_missing_values(self, method: str = 'ffill') -> None:
        """
        Handle missing values in the data.
        
        Parameters:
        -----------
        method : str
            Method to handle missing values ('ffill', 'bfill', 'drop')
        """
        for ticker in self.tickers:
            if ticker in self.data:
                if method == 'ffill':
                    self.data[ticker] = self.data[ticker].fillna(method='ffill').fillna(method='bfill')
                elif method == 'bfill':
                    self.data[ticker] = self.data[ticker].fillna(method='bfill').fillna(method='ffill')
                elif method == 'drop':
                    self.data[ticker] = self.data[ticker].dropna()
    
    def get_combined_returns(self) -> pd.DataFrame:
        """
        Get a combined DataFrame of daily returns for all assets.
        
        Returns:
        --------
        pd.DataFrame
            DataFrame with daily returns for all assets
        """
        returns_dict = {}
        for ticker in self.tickers:
            if ticker in self.data and 'Daily_Return' in self.data[ticker].columns:
                returns_dict[ticker] = self.data[ticker]['Daily_Return']
        
        return pd.DataFrame(returns_dict)
    
    def save_data(self, output_dir: str = '../data/processed/') -> None:
        """
        Save processed data to CSV files.
        
        Parameters:
        -----------
        output_dir : str
            Directory to save the files
        """
        import os
        os.makedirs(output_dir, exist_ok=True)
        
        for ticker in self.tickers:
            if ticker in self.data:
                output_path = f'{output_dir}{ticker}_processed.csv'
                self.data[ticker].to_csv(output_path)
                print(f"✓ Saved {ticker} data to {output_path}")
        
        # Save combined returns
        returns_df = self.get_combined_returns()
        returns_path = f'{output_dir}all_returns.csv'
        returns_df.to_csv(returns_path)
        print(f"✓ Saved combined returns to {returns_path}")


def load_processed_data(ticker: str, data_dir: str = '../data/processed/') -> pd.DataFrame:
    """
    Load processed data for a specific ticker.
    
    Parameters:
    -----------
    ticker : str
        Ticker symbol
    data_dir : str
        Directory containing processed data
        
    Returns:
    --------
    pd.DataFrame
        Processed data for the ticker
    """
    file_path = f'{data_dir}{ticker}_processed.csv'
    return pd.read_csv(file_path, index_col=0, parse_dates=True)


# Example usage
if __name__ == "__main__":
    # Initialize loader
    loader = FinancialDataLoader(
        tickers=['TSLA', 'BND', 'SPY'],
        start_date='2015-01-01',
        end_date='2026-01-15'
    )
    
    # Download data
    data = loader.download_data()
    
    # Add returns
    loader.add_returns()
    
    # Handle missing values
    loader.handle_missing_values()
    
    # Save processed data
    loader.save_data()
    
    print("\nData loading and processing completed!")
