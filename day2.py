import pandas as pd

df = pd.read_csv(r"C:\Users\shrub\OneDrive\Desktop\fake job detection\dataset\fake_job_postings.csv")

print(df.head())
print("\nShape:", df.shape)

print("\nInfo:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())