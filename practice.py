# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 15:03:53 2021

@author: zachk
"""

import pandas as pd
import numpy as np
from openpyxl.workbook import Workbook

# df = pd.read_excel('Modified.xlsx')

# print(df)

# # print(df.iloc[1])

# df['Test Col'] = False

# print(df)

# print(df.loc[df[1] == 'Jack'])

df = pd.read_csv('Names.csv', header=None)

# Creat column headers since the csv file doesn't have any
df.columns = ['First','Last','Address','City','State','Area Code', 'Income']

# Drop the address column
df.drop(columns='Address', inplace=True)

# Check to make sure there are no issues
# print(df)

df = df.set_index('Area Code')

#Used the Area Code column as an index and displayed the information of that area code
# print(df.loc[8074])

# Used an ":" to start at 8074 and continue through out that column until the end while 
# displaying the "First" column as well
# print(df.loc[8074:, 'First'])

# Repeated the above but with different inputs to get a feel for locating data with pandas
print(df.loc[9119:298, 'Last'])