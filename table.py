# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 10:37:54 2021

@author: zachk
"""

from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.drawing.image import Image
from openpyxl import load_workbook

wb = load_workbook('Pie.xlsx')
ws = wb.active

#Create a table named 'Table1'
tab = Table(displayName='Python_Created_Table', ref='A1:B5')
#Create the table style
style = TableStyleInfo(name='TableStyleMedium13', showFirstColumn=False, showLastColumn=False, showRowStripes=True, showColumnStripes=True)
#Input the table style just created above
tab.tableStyleInfo = style
#Add the table to the worksheet
ws.add_table(tab)
#Save the workbook
wb.save('table.xlsx')

img = Image('madecraft.jpg')
img.height = img.height * .50
img.width = img.width * .50
ws.add_image(img, 'L1')
wb.save('image.xlsx')