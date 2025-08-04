import pandas as pd
import numpy as np

position = input("What position do you want to generate a consistency ranking of? ")

# Load the CSV file
df = pd.read_csv(f"Data/{position}.csv")

# Define the week columns
weeks = [str(week) for week in range(1, 19)]

# Clean the weekly data
df[weeks] = df[weeks].replace(["BYE", "-"], np.nan)
df[weeks] = df[weeks].astype(float)

# Calculate standard deviation and coefficient of variation
df['STD'] = df[weeks].std(axis=1)
df['CV'] = df['STD'] / df['AVG']

# Filter players with AVG > 7
df = df[df['AVG'] > 7]

# Sort by lowest CV
df = df.sort_values(by='CV', ascending=True)

# Export to Excel
df.to_excel(f"{position}_Consistency_Rankings.xlsx", index=False)
