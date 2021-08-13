# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 19:33:23 2021

@author: zachk
"""

import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font

df_1 = pd.read_excel('shifts.xlsx', sheet_name='Sheet')
df_2 = pd.read_excel('shifts.xlsx', sheet_name='Sheet1')
df_3 = pd.read_excel('shift_3.xlsx')

#combine all 3 of the sheets listed above in to one data frame
df_all = pd.concat([df_1, df_2, df_3], sort=False)

print(df_all)
#group combined df by the 'Shift' column and list the mean of 'Units Sold' column with this grouping
print(df_all.groupby(['Shift']).mean()['Units Sold'])
#group combined df by the 'Region' column and list the sum of the 'Units Sold' with this grouping
print(df_all.groupby(['Region']).sum(['Units Sold']))
# print(df_all.groupby(['Shift']).mean(['Units Sold']))

# to_excel = df_all.to_excel('all_shifts.xlsx', index=None)


wb = load_workbook('all_shifts.xlsx')
ws = wb.active

total_col = ws['G1']
total_col.font = Font(bold=True)
total_col.value = 'Total'

e_col, f_col = ['E', 'F']
for row in range(2,300):
    result_cell = 'G{}'.format(row)
    e_value = ws[e_col + str(row)].value
    f_value = ws[f_col + str(row)].value
    ws[result_cell] = e_value * f_value

wb.save('totaled.xlsx')