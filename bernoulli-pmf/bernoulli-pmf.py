import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    pmf = []

    for value in x:
        if value == 0:
            pmf.append(1 - p)
        else:  
            pmf.append(p)

    mean = p
    variance = p * (1 - p)

    return {
        "pmf": np.array(pmf),
        "mean": float(mean),
        "variance": float(variance)
    }