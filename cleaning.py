# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 10:33:18 2021

@author: zachk
"""

import pandas as pd
# from openpyxl.workbook import Workbook
import numpy as np

df = pd.read_csv('Names.csv', header=None)

# Creat column headers since the csv file doesn't have any
df.columns = ['First','Last','Address','City','State','Area Code', 'Income']

# Drop the address column
df.drop(columns='Address', inplace=True)

# Check to make sure there are no issues
# print(df)

df = df.set_index('Area Code')

#Call on the object 'First' Column and seperate the strings into new columns 
# print(df.First.str.split(expand=True))
# #Call on the object 'First' Column and seperate the strings in the 'First' Column with commas 
# print(df.First.str.split(expand=False))

df.First = df.First.str.split(expand=False)

print(df)

#Remove Nan values
df = df.replace(np.nan, 'N/A', regex=True)

print(df)