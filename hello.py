import pandas as pd
from openpyxl.workbook import Workbook

pd.set_option('display.max_columns', 10)

df_excel = pd.read_excel('regions.xlsx')
df_csv = pd.read_csv('Names.csv', header=None)
df_txt = pd.read_csv('data.txt', delimiter='\t')

df_csv.columns = ['First','Last','Address','City','State','Area','Code']

# df_csv.to_excel('Modified.xlsx')
# print(df_excel)
# print(df_csv)
# print(df_csv)

# wanted_values = df_csv[['Last','Area','City']]
# wanted_values.to_excel('df_csv_test1.xlsx', index=None)

print(df_csv.iloc[3])