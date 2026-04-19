import pandas as pd

# Load cleaned data
df = pd.read_csv("data/cleaned_churn.csv")

# Separate target
y = df["Churn"]
X = df.drop("Churn", axis=1)

# Convert categorical columns
X = pd.get_dummies(X, drop_first=True)

print("Shape of X:", X.shape)
print("Shape of y:", y.shape)

# Save processed data
X.to_csv("data/X.csv", index=False)
y.to_csv("data/y.csv", index=False)