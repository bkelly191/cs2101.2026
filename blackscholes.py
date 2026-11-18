"""the Black-Scholes price of a European call option,
as developed in Notebook 9
"""

import numpy as np
from scipy.special import erf


def phi(x):
    """the cumulative distribution function of the standard normal
    distribution
    """
    return 0.5 * (1 + erf(x / np.sqrt(2)))


def BS_price(S, K, r, sigma, T):
    """the Black-Scholes price of a European call option

    S: stock price, K: strike, r: interest rate,
    sigma: volatility, T: time to maturity
    """
    d1 = ((np.log(S / K) + (r + 0.5 * sigma**2) * T)
          / (sigma * np.sqrt(T)))
    d2 = d1 - sigma * np.sqrt(T)
    return S * phi(d1) - K * np.exp(-r * T) * phi(d2)
