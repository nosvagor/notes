#!/usr/bin/env python
# coding: utf-8

# # COURSE: A deep understanding of deep learning
# ## SECTION: Math prerequisites
# ### LECTURE: Derivatives: intuition and polynomials
# #### TEACHER: Mike X Cohen, sincxpress.com
# ##### COURSE URL: udemy.com/course/dudl/?couponCode=202201

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt

# sympy = symbolic math in Python
import sympy as sym
import sympy.plotting.plot as symplot


# In[ ]:


# create symbolic variables in sympy
x = sym.symbols('x')

# create a function
fx = 2*x**2

# compute its derivative
df = sym.diff(fx,x)

# print them
print(fx)
print(df)


# In[ ]:


# plot them
symplot(fx,(x,-4,4),title='The function')
plt.show()

symplot(df,(x,-4,4),title='Its derivative')
plt.show()


# In[ ]:


# repeat with relu and sigmoid

# create symbolic functions
relu = sym.Max(0,x)
sigmoid = 1 / (1+sym.exp(-x))

# graph the functions
p = symplot(relu,(x,-4,4),label='ReLU',show=False,line_color='blue')
p.extend( symplot(sigmoid,(x,-4,4),label='Sigmoid',show=False,line_color='red') )
p.legend = True
p.title = 'The functions'
p.show()


# graph their derivatives
p = symplot(sym.diff(relu),(x,-4,4),label='df(ReLU)',show=False,line_color='blue')
p.extend( symplot(sym.diff(sigmoid),(x,-4,4),label='df(Sigmoid)',show=False,line_color='red') )
p.legend = True
p.title = 'The derivatives'
p.show()

