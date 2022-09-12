# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from scipy.interpolate import lagrange  
import matplotlib.pyplot as plt
x=[0.6,0.8,1.6,1.8,4.6,5]
y=[4.5445,6.0862,23.9912,33.9240,225.4833,79.3074]
plt.plot(x,y,"o")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
p=lagrange(x, y)
print(p)
print("evaluar en x")
print(p(1.7))
