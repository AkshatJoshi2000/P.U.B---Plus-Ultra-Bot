import numpy as np

def coinFlip():
    p = .5
    result = np.random.binomial(1,p)
    return result

def method(dict, value):
    keys = list(dict.keys())
    vals = list(dict.values())
    return keys[vals.index(value)]
