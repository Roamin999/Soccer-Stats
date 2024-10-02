import pandas as pd

df = pd.read_csv('top5-players.csv')

columns_to_drop = ['G-PK', 'PK', 'PKatt','xG','npxG','xAG','npxG+xAG','PrgC','PrgP','PrgR','Age','Born','G-PK_90','G+A-PK_90','xG_90','xAG_90','xG+xAG_90','npxG_90','npxG+xAG_90']
df = df.drop(columns=columns_to_drop)

df.to_csv('foot_but_cleaned.csv', index=False)