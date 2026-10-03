import numpy as np


def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    n = len(x) 

    mean = sum(x)/n

    var = sum((xi - mean) ** 2 for xi in x) / (n - 1)

    dev = np.sqrt(var)

    return {
        "variance":float(var),
        "standard_deviation":float(dev)
    }

    # return {
    #     "variance": float(np.var(x, ddof=1)),
    #     "standard_deviation": float(np.std(x, ddof=1)),
    # }
    # ddof=1 to use sample variance
    # population variance : var = sum((xi - mean) ** 2 for xi in x) / n