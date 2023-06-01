#!/usr/bin/env python
# coding: utf-8

# In[6]:


from pyteomics import mgf
import sys

#Selectable approach


#File path
file = mgf.read('/Users/henriksogaard/Downloads/T0-LT2.mgf', use_index = True)
nSpectra = len(file)    

#Output file
outputFile = '/Users/henriksogaard/Downloads/mgf-test-files/T0-LT2(10).mgf'

#Set the value of n
n = 10

#Selection
for i in range(nSpectra):
    if i % n == 0:
        mgf.write([file[i]], outputFile)
        


# In[]:





