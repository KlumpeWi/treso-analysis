
import pandas as pd
import os


workspace = r"W:\Data Sharing\persons_2011.csv"

print("Loading file")
df = pd.read_csv(os.path.join(workspace, 'persons_2011.csv'))
print("Grouping by TRESO zone")
df = df[['treso_zone', 'age']].groupby('treso_zone', as_index=False).count()
df['population'] = df['age']
df = df[['treso_zone', 'population']]
print(df.head())

df.to_csv(os.path.join(workspace, 'persons_2011_by_zone.csv'), index=False)