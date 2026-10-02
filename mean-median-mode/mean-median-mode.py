from collections import Counter

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    n = len(x)

    mean = sum(x) / n

    y = sorted(x)

    if n % 2:
        median = y[n // 2]
    else:
        median = (y[n // 2 - 1] + y[n // 2]) / 2

    freq = Counter(x)
    mode = min(freq, key=lambda k: (-freq[k], k))

    return {
        "mean": float(mean),
        "median": float(median),
        "mode": float(mode),
    }