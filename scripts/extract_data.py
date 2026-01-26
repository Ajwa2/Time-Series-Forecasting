"""
Script to extract and process financial data for GMF Investments project
Run this script to download data for TSLA, BND, and SPY
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from data_loader import FinancialDataLoader


def main():
    """Main function to extract and process financial data"""
    
    print("="*60)
    print("GMF INVESTMENTS - DATA EXTRACTION")
    print("="*60)
    print("\nExtracting historical financial data...")
    print("Assets: TSLA, BND, SPY")
    print("Period: 2015-01-01 to 2026-01-15\n")
    
    # Initialize loader
    loader = FinancialDataLoader(
        tickers=['TSLA', 'BND', 'SPY'],
        start_date='2015-01-01',
        end_date='2026-01-15'
    )
    
    # Download data
    print("Step 1: Downloading data from YFinance...")
    data = loader.download_data(verbose=True)
    
    # Add returns
    print("\nStep 2: Calculating daily returns...")
    loader.add_returns()
    print("✓ Daily returns calculated for all assets")
    
    # Handle missing values
    print("\nStep 3: Handling missing values...")
    loader.handle_missing_values(method='ffill')
    print("✓ Missing values handled")
    
    # Save processed data
    print("\nStep 4: Saving processed data...")
    loader.save_data(output_dir='data/processed/')
    
    # Display summary
    print("\n" + "="*60)
    print("DATA EXTRACTION COMPLETED!")
    print("="*60)
    
    print("\nSummary:")
    for ticker in loader.tickers:
        if ticker in loader.data:
            df = loader.data[ticker]
            print(f"\n{ticker}:")
            print(f"  Trading days: {len(df)}")
            print(f"  Date range: {df.index[0].date()} to {df.index[-1].date()}")
            print(f"  Columns: {', '.join(df.columns.tolist())}")
    
    print("\n" + "="*60)
    print("Next steps:")
    print("1. Open notebooks/task1_data_exploration.ipynb")
    print("2. Run all cells to perform comprehensive EDA")
    print("3. Review visualizations and insights")
    print("="*60)


if __name__ == "__main__":
    main()
