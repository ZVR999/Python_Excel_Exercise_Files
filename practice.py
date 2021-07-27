# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 15:03:53 2021

@author: zachk
"""

import pandas as pd

df = pd.read_excel('Modified.xlsx')

print(df)

# print(df.iloc[1])

df['Test Col'] = False

print(df)




# print(df)

# print(df.loc[df[1] == 'Jack'])

