#!/usr/bin/env python
# coding: utf-8

# In[55]:


import numpy as np
import cmath
import math
import matplotlib.pyplot as plt


# 
# --- 
# # VIDEO: From the number line to the complex number plane
# ---
# 

# In[57]:


## the imaginary operator

# Python differs from MATLAB here:
1j
cmath.sqrt(-1) # note the cmath module


## creating complex numbers
z = 4 + 3j
z = 4 + 3*1j
z = 4 + 3*cmath.sqrt(-1)
z = complex(4,3)

print('Real part is ' + str(np.real(z)) + ' and imaginary part is ' + str(np.imag(z)) + '.' )


# In[34]:


## plotting a complex number

plt.plot( np.real(z),np.imag(z),'rs' )
plt.xlim([-5,5])
plt.ylim([-5,5])
plt.plot([-5,5],[0,0],'k')
plt.plot([0,0],[-5,5],'k')
plt.xlabel('real axis')
plt.ylabel('imag axis')

plt.show()


# 
# ---
# # VIDEO: Addition and subtraction with complex numbers
# ---
# 

# In[38]:



# create two complex numbers
a = complex(4,5)
b = 3+2j

# let Python do the hard work
z1 = a+b
print(z1)

# the "manual" way
z2 = complex( np.real(a)+np.real(b) , np.imag(a)+np.imag(b) )
print(z2)

## subtraction is the same as addition...

# let MATLAB do the hard work
z3 = a-b
print(z3)

# the "manual" way
z4 = complex( np.real(a)-np.real(b) , np.imag(a)-np.imag(b) )
print(z4)


# 
# ---
# # Multiplication with complex numbers
# ---
# 

# In[42]:



# create two complex numbers
a = complex(4,5)
b = 3+2j

# let MATLAB do the hard work
z1 = a*b
print(z1)

# the intuitive-but-WRONG way
z2 = complex( np.real(a)*np.real(b) , np.imag(a)*np.imag(b) )
print(str(z2)+' -- the WRONG way!')

# the less-intuitive-but-CORRECT way
ar = np.real(a)
ai = np.imag(a)
br = np.real(b)
bi = np.imag(b)

z3 = (ar + 1j*ai) * (br + 1j*bi)
z4 = (ar*br) + (ar*(1j*bi)) + ((1j*ai)*br) + ((1j*ai)*(1j*bi))

print(z3)
print(z4)


# 
# ---
# # VIDEO: The complex conjugate
# ---
# 

# In[46]:


# create a complex number

a = complex(4,-5)

# let Python do the hard work
ac1 = np.conj(a)
print(ac1)

# the "manual" way
ac2 = complex( np.real(a) , -np.imag(a) )
print(ac2)


## magnitude squared of a complex number
amag1 = a*np.conj(a) # note that Python keeps this as type==complex, although the imaginary part is zero
amag2 = np.real(a)**2 + np.imag(a)**2
amag3 = np.abs(a)**2

print( str(amag1)+'='+str(amag2)+'='+str(amag3) )


# 
# ---
# # VIDEO: Division with complex numbers
# ---
# 

# In[49]:


# create two complex numbers
a = complex(4,-5)
b = complex(7,8)

# let Python do the hard work
adb1 = a/b

# the "manual" way
adb2 = (a*np.conj(b)) / (b*np.conj(b))

print(adb1)
print(adb2)


# 
# ---
# # VIDEO: Magnitude and phase of complex numbers
# ---
# 

# In[62]:


# create a complex number
z = 4 + 3j

# plot the complex number
plt.plot(np.real(z),np.imag(z),'ks')

# make plot look nicer
plt.xlim([-5,5])
plt.ylim([-5,5])
plt.plot([-5,5],[0,0],'k')
plt.plot([0,0],[-5,5],'k')
plt.xlabel('real axis')
plt.ylabel('imag axis')
plt.show()


# magnitude of the number (distance to origin)
magZ1 = np.sqrt( np.real(z)**2 + np.imag(z)**2 )
magZ2 = np.abs( z )

# angle of the line relative to positive real axis
angZ1 = math.atan2( np.imag(z),np.real(z) )
angZ2 = np.angle( z )

# draw a line using polar notation
plt.polar([0,angZ1],[0,magZ1],'r')

plt.show()

