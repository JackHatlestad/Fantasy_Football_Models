import pandas as pd
import numpy as np

position = input("What position do you want to generate a consistency ranking of? ")

df = pd.read_csv(f"Data/{position}.csv")

weeks = [str(week) for week in range(1, 19)]

df[weeks] = df[weeks].replace(["BYE", "-"], np.nan)
df[weeks] = df[weeks].astype(float)

df['STD'] = df[weeks].std(axis=1)
df['CV'] = df['STD'] / df['AVG']

df = df[df['AVG'] > 7]

df = df.sort_values(by='CV', ascending=True)

df.to_excel(f"{position}_Consistency_Rankings.xlsx", index=False)
