#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#FINDING ROOTS USING BISECTION AND NEWTON'S METHODS
from numpy import *
from matplotlib.pyplot import plot, show

x = arange(-1, 2, 0.01) #get values between -10 and 10 with 0.01 step and set to y
y = 2.019**(-x**3)-x**5*np.sin(x**4)-1.984

plot(x, y)
show()

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 2.019**(-x**3)-x**5*np.sin(x**4)-1.984
def fprime(x):
    return -5*(x**4)-4*(x**8)*np.cos(x**4)-2.10781*np.exp(-0.702602*x**3)*x**2
def bisection(a,b,tol):
    xl = a
    xr = b
    while(np.abs(xl-xr)>=tol):
        c = (xl+xr)/2.0
        prod = f(xl)*f(xr)
        if prod > tol:
            xl = c
        else:
            if prod < tol:
                xr = c
    return c
def root(guess, interval):
    for val in interval:
        nextGuess = guess -f(guess)/fprime(guess)
        guess = nextGuess
    print("Root X is "+str(round(nextGuess,4)))

lst = [[-1,-0.8],[1.3,1.4],[1.5,1.6],[1.7,1.8],[1.8,1.9],[1.9,2]]
guess = [-0.9,1.37,1.55,1.75,1.85,1.95]
lst_len = len(lst)
print("The roots of our function on [-1,2] are the following:\n")
for i in range(lst_len):
    print("Root #"+str(i)+":\n")
    root(guess[i], lst[i])
    answer = bisection(lst[i][0],lst[i][1],1e-8)
    print("Bisection Method gives approximation for the "+str(i)+" root x = "+str(answer)+"\n")
    print("Rounded bisection method roots are:"+str(round(answer,4)))

