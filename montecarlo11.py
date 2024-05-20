
import pandas as pd
import numpy as np
from scipy.stats import norm

# Load historical Bitcoin price data
btc_data = pd.read_csv('bitcoin_prices.csv', parse_dates=['Date'], index_col='Date')

# Calculate log returns
btc_data['LogReturns'] = np.log(btc_data['Close'] / btc_data['Close'].shift(1))

# Calculate mean and standard deviation of log returns
mu = btc_data['LogReturns'].mean()
sigma = btc_data['LogReturns'].std()

# Define trading strategy parameters
trading_days = 252
initial_capital = 10000
num_simulations = 10000

# Monte Carlo simulation
portfolio_values = []
for _ in range(num_simulations):
    daily_returns = np.random.normal(mu, sigma, trading_days)
    portfolio_value = initial_capital
    for return_val in daily_returns:
        portfolio_value *= (1 + return_val)
    portfolio_values.append(portfolio_value)

# Calculate strategy performance metrics
portfolio_values = np.array(portfolio_values)
avg_portfolio_value = portfolio_values.mean()
std_portfolio_value = portfolio_values.std()
sharpe_ratio = (avg_portfolio_value - initial_capital) / (std_portfolio_value * np.sqrt(trading_days))

# Calculate Value-at-Risk (VaR) and Conditional Value-at-Risk (CVaR)
sorted_portfolio_values = np.sort(portfolio_values)
var_95 = sorted_portfolio_values[int(0.05 * num_simulations)]
cvar_95 = sorted_portfolio_values[:int(0.05 * num_simulations)].mean()

# Print strategy performance metrics
print(f"Average Portfolio Value: ${avg_portfolio_value:.2f}")
print(f"Standard Deviation of Portfolio Value: ${std_portfolio_value:.2f}")
print(f"Sharpe Ratio: {sharpe_ratio:.4f}")
print(f"95% Value-at-Risk (VaR): ${var_95:.2f}")
print(f"95% Conditional Value-at-Risk (CVaR): ${cvar_95:.2f}")
