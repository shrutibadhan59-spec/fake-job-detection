import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset load
df = pd.read_csv(r"dataset\fake_job_postings.csv")

# -----------------------------
# 1. Pie Chart (Real vs Fake Jobs)
# -----------------------------
plt.figure(figsize=(6,6))
df["fraudulent"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    labels=["Real Jobs", "Fake Jobs"]
)
plt.title("Real vs Fake Job Distribution")
plt.ylabel("")
plt.show()

# -----------------------------
# 2. Correlation Heatmap
# -----------------------------
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# -----------------------------
# 3. Top 10 Industries
# -----------------------------
plt.figure(figsize=(10,6))
df["industry"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Industries")
plt.xlabel("Industry")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# 4. Employment Type
# -----------------------------
plt.figure(figsize=(8,5))
df["employment_type"].value_counts().plot(kind="bar")
plt.title("Employment Type Distribution")
plt.xlabel("Employment Type")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("Advanced Visualization Completed Successfully!")