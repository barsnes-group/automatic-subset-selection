#!/usr/bin/env python
# coding: utf-8

# In[19]:


from pyteomics import mgf
import sys
import random

#Randomized approach

#File path
file = mgf.read('/Users/henriksogaard/Downloads/split_test/split-test.mgf', use_index = True)
nSpectra = len(file) 

#Output file
outputFile = '/Users/henriksogaard/Downloads/mgf-test-files/mgf-test(random1134(10)).mgf'

#List for creating random indexes
indexList = random.sample(range(0, nSpectra), 1134)

#Add spectra to output file
for i in range(len(indexList)):
    mgf.write([file[indexList[i]]], outputFile)


# In[ ]:




