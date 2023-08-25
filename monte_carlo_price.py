
import numpy as np
from scipy.stats import norm

def monte_carlo_asian_call_option(S0, K, r, sigma, T, n, m):
    dt = T / n
    daily_steps = int(T * 365)
    total_payoff = 0

    for _ in range(m):
        price_path = np.zeros(daily_steps + 1)
        price_path[0] = S0
        arithmetic_mean = S0


    sum_prices = S0
    for i in range(1, daily_steps + 1):
        z = np.random.randn()
        price_path[i] = price_path[i - 1] * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z)
        sum_prices += price_path[i]
        arithmetic_mean = sum_prices / (daily_steps + 1)

        # for i in range(1, daily_steps + 1):
        #     z = np.random.randn()
        #     price_path[i] = price_path[i - 1] * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z)
        #     arithmetic_mean = (i * arithmetic_mean + price_path[i]) / (i + 1)

        payoff = max(arithmetic_mean - K, 0)
        total_payoff += payoff

    option_price = np.exp(-r * T) * (total_payoff / m)
    return option_price

def analytic_asian_call_option(S0, K, r, sigma, T, n):
    a = r * (n + 1) * (2 * n + 1) / (6 * 365 * 365)
    b = 0.5 * sigma**2 * (n + 1)**2 / (365 * 365)
    c = a - b
    d1 = (np.log(S0 / K) + (c + 0.5 * b) * T) / np.sqrt(b * T)
    d2 = d1 - np.sqrt(b * T)

    option_price = np.exp(-r * T) * (S0 * np.exp(c * T) * norm.cdf(d1) - K * norm.cdf(d2))
    return option_price

# Parameters
S0 = 100    # Initial stock price
K = 105     # Strike price
r = 0.05    # Risk-free rate
sigma = 0.3 # Volatility
T = 2       # Time to maturity
n = 10000   # Number of averaging periods
m = 100000  # Number of simulations

monte_carlo_price = monte_carlo_asian_call_option(S0, K, r, sigma, T, n, m)
analytic_price = analytic_asian_call_option(S0, K, r, sigma, T, n)

print("Monte Carlo Asian Call Option Price:", monte_carlo_price)
print("Analytic Asian Call Option Price:", analytic_price)
#code.txt
#Displaying code.txt.