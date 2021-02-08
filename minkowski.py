#!/usr/bin/env python
# coding=utf-8

import numpy as np
from numpy import random as rd

import utils as u

def L_p(xi, xj, p):
    u.p_msg(p)
    
    diff = np.abs(xi-xj)
    nsum = np.sum(np.power(diff, p)) 
    if p != 0:
        dist = np.power(nsum, np.divide(1, p))
        print(dist)
        return dist

L_p(rd.random(10), rd.random(10), 0)
L_p(rd.random(10), rd.random(10), 1)
L_p(rd.random(10), rd.random(10), 2)
