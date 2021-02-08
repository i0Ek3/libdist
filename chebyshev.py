#!/usr/bin/env python
# coding=utf-8

import numpy as np
from numpy import random as rd

def chebyshev(x, y):
    diff = np.abs(x-y)
    dist = np.max(diff)
    return dist

print(rd.random(10), rd.random(10))
