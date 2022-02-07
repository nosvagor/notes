#!/usr/bin/env python
# coding: utf-8

# # COURSE: A deep understanding of deep learning
# ## SECTION: More on data
# ### LECTURE: Getting data into colab
# #### TEACHER: Mike X Cohen, sincxpress.com
# ##### COURSE URL: udemy.com/course/dudl/?couponCode=202201

# In[ ]:





# # Import from torchvision

# In[ ]:


import torchvision

# download the CIFAR10 dataset
cdata = torchvision.datasets.CIFAR10(root='cifar10', download=True)

print(cdata)


# In[ ]:


# Datasets that come with torchvision: https://pytorch.org/vision/stable/index.html


# # Download from the web

# In[ ]:


import pandas as pd

# url
marriage_url = 'https://www.cdc.gov/nchs/data/dvs/state-marriage-rates-90-95-99-19.xlsx'

# import directly into pandas
data = pd.read_excel(marriage_url,header=5)
data


# In[ ]:





# # Upload from hard drive

# In[ ]:


from google.colab import files
uploaded = files.upload()


# In[ ]:





# # Map your google-drive

# In[ ]:


from google.colab import drive
drive.mount('/content/gdrive')


# In[ ]:




