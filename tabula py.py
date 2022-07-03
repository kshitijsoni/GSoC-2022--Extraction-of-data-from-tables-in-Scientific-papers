#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install tabula-py


# In[2]:


pip install tabulate


# In[3]:


from tabula import read_pdf


# In[11]:


from tabulate import tabulate
import tabula


# In[12]:


import pandas as pd


# In[13]:


import io


# In[79]:


tableextr = read_pdf('00028727_Gilchrist06.pdf', pages = 7, multiple_tables = True, stream = True)


# In[80]:


table = tabulate(tableextr)


# In[81]:


df = pd.read_fwf(io.StringIO(table))


# In[82]:


df.to_excel("test5.xlsx")


# In[74]:


import csv

with open('test5.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file, delimiter=';')
    writer.writerow('my_utf8_string')


# In[83]:


tabula.convert_into('00028727_Gilchrist06.pdf', "test5.csv", 
                    output_format="csv", pages = 7)


# In[ ]:




