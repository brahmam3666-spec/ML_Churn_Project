import pandas as pd

df = pd.read_csv("data/churn.csv")

print("shape:", df.shape)

print("\nColumns\n:", df.columns)

print("\nFirst 5 rows\n:", df.head())