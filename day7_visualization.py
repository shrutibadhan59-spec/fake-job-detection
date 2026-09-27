import pandas as pd
import matplotlib.pyplot as plt

# Dataset load
df = pd.read_csv(r"dataset\fake_job_postings.csv")

# 1. Class Distribution
df["fraudulent"].value_counts().plot(kind="bar")

plt.title("Real vs Fake Jobs")
plt.xlabel("Fraudulent (0 = Real, 1 = Fake)")
plt.ylabel("Count")
plt.show()

# 2. Missing Values
missing = df.isnull().sum()
missing = missing[missing > 0]

missing.sort_values().plot(kind="barh")

plt.title("Missing Values")
plt.xlabel("Count")
plt.show()