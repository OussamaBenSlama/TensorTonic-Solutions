import numpy as np

def t_test_one_sample(x: list, mu0: float) -> float:
    """
    Returns the t-statistic as a float.
    """
    n = len(x)
    mean = sum(x) / n

    var = (1/(n-1)) * sum([(xi - mean)**2 for xi in x])

    dev = np.sqrt(var)

    if dev == 0:
        if mean == mu0:
            return 0.0
        return float(np.inf if mean > mu0 else -np.inf)

    t = (mean - mu0)/(dev/np.sqrt(n))

    return float(t)