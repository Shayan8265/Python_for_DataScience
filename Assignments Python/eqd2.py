#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
Sample module provided for the Python Data Lab, Fall 2022.
'''
import numpy as np

def eqdistgrid(xinit,N,deltax=1):
    '''
    Create equidistant numerical grid.
    Arguments
    * xinit  : initial grid coordinate.
    * N      : total number of grid points.
    Keyword arguments
    * deltax : grid spacing.
    On return
    * grid   : equidistant numerical grid.
    '''
    grid = np.linspace(xinit,xinit+(N-1)*deltax,N)
    return grid

def eqdistdif1(f,deltax=1):
    '''
    Centered differencing approximation of the first derivative 
    for the interior points of an equidistant grid.
    Arguments
    * f      : grid function.
    Keyword arguments
    * deltax : grid spacing.
    On return
    * dfodx : approximation of the first derivative.
    '''
    df = f[2:] - f[:-2]
    dfodx = df/(2*deltax)
    return dfodx


# In[ ]:


def eqdistdif2(f,deltax=1):
    '''
    Centered differencing approximation of the second derivative 
    for the interior points of an equidistant grid.
    Arguments
    * f       : grid function.
    Keyword arguments
    * deltax  : grid spacing.
    On return
    * d2fodx2 : approximation of the second derivative.
    '''
    d2f = f[2:] - 2*f[1:-1] + f[:-2]
    d2fodx2 = d2f/(deltax**2)
    return d2fodx2

