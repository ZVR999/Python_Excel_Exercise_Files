# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 10:57:53 2021

@author: zachk
"""


import pandas as pd
from openpyxl.workbook import Workbook

pd.set_option('display.max_rows', 50)

df = pd.read_csv('Names.csv', header=None)

df.columns = ['First','Last','Address','City','State','Area','Code']

# print(df.iloc[3,2])

wanted_values = df[['First','Last','State']]
stored = wanted_values.to_excel('State_Location.xlsx', index=None)