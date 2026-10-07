import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the Pearson correlation matrix as a NumPy array.
    """
    X = np.asarray(X, dtype=float)

    n = X.shape[0]

    mean = np.mean(X, axis=0)

    xc = X - mean

    sigma = (xc.T @ xc) / (n - 1)

    std = np.sqrt(np.diag(sigma))

    denominator = np.outer(std, std)

    R = np.full_like(sigma, np.nan, dtype=float)

    valid = denominator != 0
    R[valid] = sigma[valid] / denominator[valid]

    return R