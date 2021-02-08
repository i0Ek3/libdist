#!/usr/bin/env python
# coding=utf-8

import numpy as np
from numpy import random as rd

def hamming(x, y):
    nsum = np.sum(x != y)
    dist = nsum / len(x)
    return dist

print(hamming(rd.random(10), rd.random(10)))
