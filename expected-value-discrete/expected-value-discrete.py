import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    n = len(x) 

    res = 0 

    for i in range(n) :
        res += x[i]*p[i]

    return float(res)