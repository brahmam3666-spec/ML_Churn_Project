import pandas as pd

df = pd.read_csv("data/churn.csv")

# 1. Drop customerID (not useful)
df.drop("customerID", axis=1, inplace=True)

# 2. Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# 3. Handle missing values
df["TotalCharges"].fillna(df["TotalCharges"].median(), inplace=True)

# 4. Convert target variable
df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

print(df.head())
print("\nMissing values:\n", df.isnull().sum())


df.to_csv("data/cleaned_churn.csv", index=False)