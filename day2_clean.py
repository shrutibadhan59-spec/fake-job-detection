import pandas as pd

# Load Dataset
df = pd.read_csv(r"C:\Users\shrub\OneDrive\Desktop\fake job detection\dataset\fake_job_postings.csv")

# Fill Missing Values
df.fillna("Not Available", inplace=True)

# Keep Important Columns
df = df[[
    "title",
    "company_profile",

    "description",
    "requirements",
    "benefits",
    "fraudulent"
]]

# Save Clean Datasetimport pandas as pd
# Save Clean Dataset
df.to_csv(r"C:\Users\shrub\OneDrive\Desktop\fake job detection\dataset\clean_dataset.csv", index=False)

print("✅ Dataset Cleaned Successfully!")
print(df.head())
print(df.shape)