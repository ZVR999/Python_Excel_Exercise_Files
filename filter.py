import pandas as pd

df = pd.read_csv('Names.csv', header=None)

df.columns = ['First','Last','Address','City','State','Area Code','Income']

# print(df)

# print(df.loc[df['First'] == 'Jack'])

print(df.loc[df['Income'] > 20000])

# print(df['State'][1:3])

print(df.iloc[1])

values_to_save = df.iloc[1]

saved_Values = values_to_save.to_excel('Values_to_save_Test1.xlsx', index=None)
