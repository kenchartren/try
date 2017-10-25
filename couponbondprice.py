#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 15:51:39 2017

@author: steven
"""

'''
Give plot of price jump of coupon bonds with respect to time
'''

import numpy as np

import matplotlib.pyplot as plt
from math import *

# parameters of coupon bond
Pr = 1000
c = 0.05
y = 0.08
dt = 0.5
n = 20
year = int(n * dt)
step = 2 ** 8

# procedure
cashinflow = np.array(np.zeros(n + 1))
for i in range(1, n + 1):
    if i < n:
        cashinflow[i] = c * Pr * dt
    else:
        cashinflow[i] = (1 + c * dt) * Pr
        
t = np.array([i / step for i in range(step * year + 1)])
j = t // dt
Bc = np.zeros(step * year + 1)
for time in range(step * year + 1):
    for i in range(int(j[time]) + 1, n + 1):
        Bc[time] += cashinflow[i] / ((1 + y * dt) ** (i - t[time] / dt))
Bc[time] = cashinflow[n]
        
plt.plot(t, Bc)
#plt.legend()
plt.show()
# plt.hist(np.array([i for i in range(n + 1)]),cashinflow)
