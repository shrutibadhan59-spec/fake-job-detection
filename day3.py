import pandas as pd

# Load Clean Dataset
df = pd.read_csv(r"C:\Users\shrub\OneDrive\Desktop\fake job detection\dataset\clean_dataset.csv")

# Combine all text columns into one
df["text"] = (
    df["title"].astype(str) + " " +
    df["company_profile"].astype(str) + " " +
    df["description"].astype(str) + " " +
    df["requirements"].astype(str) + " " +
    df["benefits"].astype(str)
)

# Keep only text and target column
df = df[["text", "fraudulent"]]

# Save Final Dataset
df.to_csv(r"C:\Users\shrub\OneDrive\Desktop\fake job detection\dataset\final_dataset.csv", index=False)

print("✅ Text Combined Successfully!")
print(df.head())
print("\nShape:", df.shape)