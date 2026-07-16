import yfinance as yf
import numpy as np
import pandas as pd
import numpy.typing as npt
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

def load_returns(ticker: str, start_date: str, end_date: str) -> pd.Series:
    """
    Download price data and calculate daily returns.

    Args:
        ticker: Yahoo Finance ticker, e.g. "^GSPC" or "AAPL".
        start_date: Start date as YYYY-MM-DD.
        end_date: End date as YYYY-MM-DD.
    """
    data = yf.download(tickers=ticker, start=start_date, end=end_date, auto_adjust=True)
    returns = data["Close"].pct_change().dropna().squeeze()
    return returns


def investment_simulation(days: int, initial_amount: float, historic_returns: pd.Series) -> np.float64:
    sampled_returns = rng.choice(historic_returns, size=days)
    compounded_growth_factor = np.prod(1+sampled_returns, axis=None)
    final_amount = compounded_growth_factor*initial_amount    
    return final_amount

def investment_simulations(days: int, initial_amount: float, historic_returns: pd.Series, num_trials: int) -> npt.NDArray[np.float64]:
    sampled_returns = rng.choice(historic_returns, size=(num_trials, days))
    compounded_growth_factors = np.prod(1+sampled_returns, axis=1)
    final_amounts = compounded_growth_factors*initial_amount    
    return final_amounts

def plot_final_amounts(final_amounts: npt.NDArray[np.float64]) -> None:
    plt.hist(final_amounts, bins=100, edgecolor="black")
    plt.title("Distribution of simulated final investment values")
    plt.ylabel("Frequency")
    plt.xlabel("Final amount")
    plt.show()


if __name__ == "__main__":
    returns_SP = load_returns("^GSPC", "2016-01-01", "2026-01-01")
    outcome = investment_simulations(100, 100, returns_SP, 100_000)
    plot_final_amounts(outcome)

    
    