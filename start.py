#!/usr/bin/env python
# coding: utf-8

# # ~Title~

# ## Stock Imports

# ### IDE Stuff

# In[ ]:


# Jupyter Plugins that make things much nicer:
# * Collapsible_Headings
# * hide_code
# * jupyterlab-code-cell-collapser
# * jupyterlab_templates


# In[ ]:


# Code for installing packages
# !conda install --yes --prefix {sys.prefix} sympy
# !{sys.executable} -m pip install sympy


# In[ ]:


get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')


# ### Python Libraries

# In[ ]:


# System Imports
import os, sys, time


# In[ ]:


from functools import (reduce, lru_cache, partial)


# In[ ]:


# from toolz.itertoolz import ()
from toolz.functoolz import (curry)
# from toolz.dicttoolz import ()


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


# In[ ]:


from IPython.display import clear_output


# In[ ]:


import bokeh
from bokeh.io import output_notebook
from bokeh.plotting import figure, show
output_notebook()
bokeh.io.curdoc().theme = 'dark_minimal'


# ## Code Snippets

# ### Cell Updating

# In[ ]:


if False:
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
show(fig)


# In[ ]:


del ts, xs, ys, fig


# In[ ]:




