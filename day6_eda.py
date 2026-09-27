import pandas as pd

# Dataset load
df = pd.read_csv(r"dataset\fake_job_postings.csv")

# First 5 rows
print("\n===== FIRST 5 ROWS =====")
print(df.head())

# Dataset shape
print("\n===== SHAPE =====")
print(df.shape)

# Column names
print("\n===== COLUMNS =====")
print(df.columns)

# Dataset information
print("\n===== INFO =====")
print(df.info())

# Missing values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# Duplicate rows
print("\n===== DUPLICATE ROWS =====")
print(df.duplicated().sum())

# Fake vs Real jobs
print("\n===== CLASS DISTRIBUTION =====")
print(df["fraudulent"].value_counts())

# Summary statistics
print("\n===== SUMMARY =====")
print(df.describe(include="all"))