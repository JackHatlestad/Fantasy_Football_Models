import pandas as pd
import numpy as np

position = input("What position do you want to generate a consistency ranking of?\n")

df = pd.read_csv(f"{position}.csv")

weeks = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18']

for week in weeks:
    df[week] = df[week].replace(['-', 'BYE'], np.nan)
    df[week] = pd.to_numeric(df[week], errors='coerce')

numeric_cols = df[weeks]

df['STD'] = df[numeric_cols].std(axis=1)
df['ConsistencyRank'] = df['STD'].rank(ascending=True, method='min').astype(int)

print(df[['Player', 'STD', 'ConsistencyRank']].head())