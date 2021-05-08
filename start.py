#!/usr/bin/env python
# coding: utf-8

# # Setup

# ## Stock Imports

# ### IDE Stuff

# #### Installing New Packages

# In[ ]:


# Jupyter Plugins that make things much nicer:
# * Collapsible_Headings
# * hide_code
# * jupyterlab-code-cell-collapser
# * jupyterlab_templates


# In[ ]:


# Code for installing packages
# !conda install --yes --prefix {sys.prefix} PACKAGE_NAME
# !{sys.executable} -m pip install PACKAGE_NAME


# #### Notebook Customization

# In[ ]:


from IPython.display import HTML
css_str = """
<link rel="preconnect" href="https://fonts.gstatic.com">

<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600&family=Playfair+Display+SC&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lora">
<link href="https://fonts.googleapis.com/css2?family=IM+Fell+Double+Pica:ital@1&display=swap" rel="stylesheet">
    <style>
h1 { color: #7c795d; font-family: 'Playfair Display SC', serif; text-indent: 00px; text-align: center;}
h2 { color: #7c795d; font-family: 'Lora', serif;                text-indent: 00px; text-align: left; }
h3 { color: #7c795d; font-family: 'IM Fell Double Pica', serif; text-indent: 15px; text-align: left; }
h4 { color: #7c795d; font-family: 'Lora', Arial, serif;         text-indent: 30px; text-align: left}
h5 { color: #71a832; font-family: 'IM Fell Double Pica', serif; text-indent: 45px; text-align: left}

"""
HTML(css_str)


# In[ ]:





# In[ ]:


get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')


# ### Python Libraries

# In[ ]:


# System Imports
import os, sys, time


# In[ ]:


mainQ =(__name__ == '__main__')
if mainQ:
    print("This is the main file")


# ### Functional Programming

# It is very common in data analysis to run data through a series of transformations, often called a "pipe".  The advantage of this is the arguments are contained with the functions and it is more readable.  For instance, in `Mathematica`, 
# 
# `H(#, 4)& @ G(#,3)& @ F(#,2)& @ 1  =>  H(G(F(1,2),3),4).`
# 
# In the former, it is clear that `3` belongs to `G`.  In the latter, you need to count parenthesis.  This typically makes use of "lambda functions" or "pure functions".  As a primarily Object Oriented Programming (OOP) language, Python doesn't natively support much of this Functional paradigm.  However, it does treat functions as objects which can be manipulated.  Given the utility of Functional Programming, there are several packages that attempt to bring it into the language, each with varying success.

# In[ ]:


# from pipetools import where, X, pipe
# 10 > (pipe | range | where(X % 2) | sum)


# In[ ]:


# from pipey import Pipeable

# Print = Pipeable(print)
# @Pipeable
# def add(a,b): return a + b
# @Pipeable
# def sqr(b): return b*b

# np.array([3, 4]) >> sqr >> add(1000)


# In[ ]:


# from toolz.itertoolz import ()
from toolz.functoolz import (curry, pipe, thread_first)
# from toolz.dicttoolz import ()


# In[ ]:


@curry
def add(x, y): return x + y
@curry
def pow(x, y): return x**y
thread_first(1, add(y=4), pow(y=2))  # pow(add(1, 4), 2)


# In[ ]:


from mini_lambda import InputVar, as_function
_ = as_function
X = InputVar('X')


# In[ ]:


_(X+3)(10)


# In[ ]:


thread_first(1, add(y=4), _(pow(x=2, y=X)))  # pow(2, add(1, 4))


# In[ ]:


thread_first(1, _(X+4), _(2**X))  # pow(add(1, 4), 2)


# In[ ]:


add4 = _(X + 4)
sqr = _(X**2)
thread_first( np.array([1,2]), add4, sqr)  # pow(add(1, 4), 2)


# ### Scientific Programming

# In[ ]:


from math import *
deg = radians(1)    # so that we can refer to 90*deg
I = 1j              # potentially neater imaginary nomenclature.


# In[ ]:


import numpy as np  # Does high performance dense array operations
import scipy as sp
import pandas as pd
import PIL 


# In[ ]:


# Python function compilization.  Makes things very fast.  Function must only include Numpy and basic Python.  No custom classes.
from numba import njit


# In[ ]:


import sympy as sp
# sp.init_printing(pretty_print=True)
# sp.init_printing(pretty_print=False)


# ### Plotting

# In[ ]:


from IPython.display import clear_output


# In[ ]:


import bokeh
from bokeh.io import output_notebook
from bokeh.plotting import figure, show
output_notebook()
bokeh.io.curdoc().theme = 'dark_minimal'


# ## Custom Imports

# In[ ]:


from UtilityMath import (plotComplexArray, 
                         RandomComplexCircularMatrix, RandomComplexGaussianMatrix,
                         PolarPlot,
                         RescaleToUnitary,
                         ReIm,
                         MatrixSqError, MatrixError, MatrixErrorNormalized)
from Logger import Logger


# ## Code Snippets

# ### Cell Updating

# In[ ]:


if mainQ and False:
    for f in range(10):
        clear_output(wait=True)
        print(f)
        time.sleep(0.5)


# ### Bokeh Simple Line Plot

# In[ ]:


ts = np.linspace(0, 4, num=300)


# In[ ]:


xs = 5.0 * ts


# In[ ]:


ys = -9.8*ts**2 + 50*ts + 0


# In[ ]:


fig = figure(x_range=(min(xs), max(xs)), y_range=(min(ys), max(ys)), 
             plot_width=800, plot_height=400,
             title='Trajectory')
fig.xaxis.axis_label = "x (m)"
fig.yaxis.axis_label = "y (m)"
fig.line(x=xs, y=ys)
if mainQ: show(fig)


# In[ ]:


del ts, xs, ys, fig


# # Work

# In[ ]:


1+1


# In[ ]:


3+4


# In[ ]:




