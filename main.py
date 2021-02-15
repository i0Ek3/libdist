#!/usr/bin/env python
# coding=utf-8

from numpy import random as rd

import chebyshev as ch
import hamming as hm
import minkowski as mk
import utils as u

def main():
    print(ch.chebyshev(rd.random(10), rd.random(10)))
    
    print(hm.hamming(rd.random(10), rd.random(10)))
    
    print(mk.L_p(rd.random(10), rd.random(10), 0))
    print(mk.L_p(rd.random(10), rd.random(10), 1))
    print(mk.L_p(rd.random(10), rd.random(10), 2))


if __name__ == '__main__':
    main()
