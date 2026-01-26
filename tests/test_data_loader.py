"""
Unit tests for data_loader module
"""

import unittest
import pandas as pd
import numpy as np
from datetime import datetime
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from data_loader import FinancialDataLoader


class TestFinancialDataLoader(unittest.TestCase):
    """Test cases for FinancialDataLoader class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.tickers = ['AAPL']  # Use single ticker for faster tests
        self.start_date = '2020-01-01'
        self.end_date = '2020-12-31'
        self.loader = FinancialDataLoader(
            tickers=self.tickers,
            start_date=self.start_date,
            end_date=self.end_date
        )
    
    def test_initialization(self):
        """Test that loader initializes correctly"""
        self.assertEqual(self.loader.tickers, self.tickers)
        self.assertEqual(self.loader.start_date, self.start_date)
        self.assertEqual(self.loader.end_date, self.end_date)
        self.assertEqual(self.loader.data, {})
    
    def test_download_data(self):
        """Test data downloading functionality"""
        data = self.loader.download_data(verbose=False)
        
        # Check that data was downloaded
        self.assertIn('AAPL', data)
        self.assertIsInstance(data['AAPL'], pd.DataFrame)
        
        # Check that expected columns exist
        expected_columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
        for col in expected_columns:
            self.assertIn(col, data['AAPL'].columns)
        
        # Check that data is not empty
        self.assertGreater(len(data['AAPL']), 0)
    
    def test_add_returns(self):
        """Test adding daily returns"""
        self.loader.download_data(verbose=False)
        self.loader.add_returns()
        
        # Check that Daily_Return column was added
        self.assertIn('Daily_Return', self.loader.data['AAPL'].columns)
        
        # Check that returns are calculated correctly (excluding first NaN)
        returns = self.loader.data['AAPL']['Daily_Return'].dropna()
        self.assertTrue(all(isinstance(x, (int, float)) for x in returns))
    
    def test_handle_missing_values(self):
        """Test missing value handling"""
        self.loader.download_data(verbose=False)
        self.loader.add_returns()
        
        # Add some artificial missing values
        self.loader.data['AAPL'].loc[self.loader.data['AAPL'].index[10], 'Close'] = np.nan
        
        # Handle missing values
        self.loader.handle_missing_values(method='ffill')
        
        # Check that no missing values remain in Close column
        self.assertEqual(self.loader.data['AAPL']['Close'].isnull().sum(), 0)
    
    def test_get_combined_returns(self):
        """Test getting combined returns DataFrame"""
        self.loader.download_data(verbose=False)
        self.loader.add_returns()
        
        combined_returns = self.loader.get_combined_returns()
        
        # Check that returns DataFrame was created
        self.assertIsInstance(combined_returns, pd.DataFrame)
        self.assertIn('AAPL', combined_returns.columns)
        self.assertGreater(len(combined_returns), 0)


class TestDataLoaderEdgeCases(unittest.TestCase):
    """Test edge cases for data loader"""
    
    def test_invalid_ticker(self):
        """Test handling of invalid ticker"""
        loader = FinancialDataLoader(
            tickers=['INVALIDTICKER123'],
            start_date='2020-01-01',
            end_date='2020-12-31'
        )
        data = loader.download_data(verbose=False)
        
        # Should still return a dictionary, but might be empty or have empty DataFrame
        self.assertIsInstance(data, dict)
    
    def test_future_date_range(self):
        """Test with future dates (should return empty or partial data)"""
        loader = FinancialDataLoader(
            tickers=['AAPL'],
            start_date='2030-01-01',
            end_date='2030-12-31'
        )
        data = loader.download_data(verbose=False)
        
        # Should handle gracefully
        self.assertIsInstance(data, dict)


if __name__ == '__main__':
    unittest.main()
