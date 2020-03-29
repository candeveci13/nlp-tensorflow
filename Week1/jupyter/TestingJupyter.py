#!/usr/bin/env python
# coding: utf-8

# # h1 Heading
# ## h2 Heading
# ### h3 Heading
# #### h4 Heading
# ##### h5 Heading
# ###### h6 Heading
# 
# ## Horizontal Rules
# 
# ___
# 
# ---

# In[ ]:


name = 'can'


# In[ ]:


name


# In[ ]:


name = 'deveci'


# In[ ]:


name


# In[ ]:


get_ipython().system('pip list')


# In[30]:


get_ipython().run_line_magic('lsmagic', '')


# In[ ]:


get_ipython().run_line_magic('pwd', '')


# In[28]:


get_ipython().system('pip install matplotlib')


# %matplotlib inline

# In[29]:


import numpy as np

# Sample from a bivariate Gaussian distribution
mean = [0,0]
cov = [[0,1],[1,0]] 
x, y = np.random.multivariate_normal(mean, cov, 10000).T
import matplotlib.pyplot as plt

hist, xedges, yedges = np.histogram2d(x,y)
X,Y = np.meshgrid(xedges,yedges)
plt.imshow(hist)
plt.grid(True)
plt.colorbar()
plt.show()


# In[31]:


get_ipython().run_cell_magic('HTML', '', '<!DOCTYPE html>\n<html>\n<head>\n<style>\nh1 {\n  color: blue;\n  font-family: verdana;\n  font-size: 300%;\n\n}\np  {\n  color: red;\n  font-family: courier;\n  font-size: 160%;\n}\n</style>\n</head>\n<body>\n\n<h1>This is a heading</h1>\n<p>This is a paragraph.</p>\n\n</body>\n</html>')


# In[33]:


get_ipython().system('pip install pandas')


# In[34]:


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10,5))
df


# In[ ]:




