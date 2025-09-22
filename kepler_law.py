import numpy as np

def period_vs_distance_fit(distances, periods):
    a = 1.0
    b = 1.0
    # TODO: Fit the power function T = a * d^b
    # Hints: 
    # 1. Apply logarithm to convert to linear model: log(T) = log(a) + b * log(d)
    # 2. Use numpy.log and numpy.polyfit (with degree 1)

    return a, b  # Return parameters of the power model

