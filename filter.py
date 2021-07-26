import pandas as pd

df = pd.read_csv('Names.csv', header=None)

df.columns = ['First','Last','Address','City','State','Area Code','Income']


print(df.loc[(df['First'] == 'Stephen') & (df['City'] == 'SomeTown')])
