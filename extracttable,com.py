#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install -U ExtractTable')


# In[2]:


from ExtractTable import ExtractTable


# In[5]:


api_key = 'WuU8kDBHlQcPQKxSLQRxWNwypLKtZ0VFBoGbwBoX'


# In[6]:


et_sess = ExtractTable(api_key)


# In[7]:


usage = et_sess.check_usage()


# In[8]:


et_sess.server_response


# In[9]:


print(usage)


# In[20]:


image_location = r'Screenshot 2022-07-03 210749.png'


# In[21]:


table_data = et_sess.process_file(filepath='Screenshot 2022-07-03 210749.png', output_format="df")


# In[22]:


table_data


# In[23]:


et_sess.save_output('Untitled Folder 1', output_format="csv")


# In[ ]:




