#!/usr/bin/env python
# coding: utf-8

# # COURSE: A deep understanding of deep learning
# ## SECTION: Gradient descent
# ### LECTURE: CodeChallenge: Unfortunate starting value
# #### TEACHER: Mike X Cohen, sincxpress.com
# ##### COURSE URL: udemy.com/course/dudl/?couponCode=202201

# In[ ]:


# import all necessary modules
import numpy as np
import matplotlib.pyplot as plt


# # Gradient descent in 1D

# In[ ]:


# function (as a function)
def fx(x):
  return np.cos(2*np.pi*x) + x**2

# derivative function
def deriv(x):
  return -2*np.pi*np.sin(2*np.pi*x) + 2*x


# In[ ]:


# plot the function and its derivative

# define a range for x
x = np.linspace(-2,2,2001)

# plotting
plt.plot(x,fx(x), x,deriv(x))
plt.xlim(x[[0,-1]])
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(['y','dy'])
plt.show()


# In[ ]:





# In[ ]:


# random starting point
localmin = np.random.choice(x,1) #np.array([0])#

# learning parameters
learning_rate = .01
training_epochs = 100

# run through training
for i in range(training_epochs):
  grad = deriv(localmin)
  localmin = localmin - learning_rate*grad

localmin


# In[ ]:


# plot the results

plt.plot(x,fx(x), x,deriv(x))
plt.plot(localmin,deriv(localmin),'ro')
plt.plot(localmin,fx(localmin),'ro')

plt.xlim(x[[0,-1]])
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(['f(x)','df','f(x) min'])
plt.title('Empirical local minimum: %s'%localmin[0])
plt.show()


# In[ ]:





# # Additional explorations

# In[ ]:


# 1) The derivative has a multiplicative factor of 2 in it. Is that constant necessary for the accuracy of the g.d. result?
#    Try removing that '2' from the derivative and see whether the model can still find the minimum. Before running the
#    code, think about what you expect to happen. Does reality match your expectations? Why is (or isn't) that factor necessary?
# 
# 2) What about the factor of '2' inside the np.sin() function? Is that important? Can you get an accurate result if you
#    remove it?
# 
# 3) Try setting the initial value to a small but non-zero number, e.g., .0001 or -.0001. Does that help the solution?
# 

