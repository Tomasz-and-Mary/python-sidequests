import yfinance as yf
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)

def load_returns(ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
    """
    Download price data for a ticker.

    Args:
        ticker: Yahoo Finance ticker, e.g. "^GSPC" or "AAPL".
        start_date: Start date as YYYY-MM-DD.
        end_date: End date as YYYY-MM-DD.
    """
    data = yf.download(tickers=ticker, start=start_date, end=end_date, auto_adjust=True)
    returns = data["Close"].pct_change().dropna()
    return returns

returns_SP = load_returns("^GSPC", "2016-01-01", "2026-01-01")

def investment_sim(days: int, initial_amount: float, historic_returns: pd.DataFrame):
    sampled_returns = rng.choice(historic_returns, size=days)
    compounded_growth_factor = np.prod(1+sampled_returns, axis=None)
    final_amount = compounded_growth_factor*initial_amount    
    return final_amount

outcome = investment_sim(100, 100, returns_SP)
print(outcome)

    
    