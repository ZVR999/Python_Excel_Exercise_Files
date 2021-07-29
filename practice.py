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
