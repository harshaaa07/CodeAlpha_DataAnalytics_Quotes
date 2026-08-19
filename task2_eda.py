"""
CodeAlpha Data Analytics Internship - Task 2
Exploratory Data Analysis (EDA)

Run:
    pip install pandas matplotlib
    python src/task2_eda.py
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/quotes_dataset.csv")

print("\n--- DATASET OVERVIEW ---")
print("Rows:", len(df))
print("Columns:", list(df.columns))
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isna().sum())
print("\nDuplicate rows:", df.duplicated().sum())

df["quote_length"] = df["quote"].str.len()
df["word_count"] = df["quote"].str.split().str.len()
df["tag_count"] = df["tags"].fillna("").apply(
    lambda x: 0 if not x else len([t for t in x.split(", ") if t])
)

print("\n--- SUMMARY STATISTICS ---")
print(df[["quote_length", "word_count", "tag_count"]].describe())

print("\n--- TOP AUTHORS ---")
print(df["author"].value_counts().head(10))

print("\n--- TOP TAGS ---")
tags = (
    df["tags"].fillna("")
    .str.split(", ")
    .explode()
    .replace("", pd.NA)
    .dropna()
)
print(tags.value_counts().head(10))

print("\n--- QUESTIONS / FINDINGS ---")
print("1. How many quotes were collected?", len(df))
print("2. Average quote length:", round(df["quote_length"].mean(), 2), "characters")
print("3. Average quote word count:", round(df["word_count"].mean(), 2))
print("4. Most frequent author:", df["author"].value_counts().idxmax())
print("5. Most common tag:", tags.value_counts().idxmax() if len(tags) else "N/A")

# Detect unusually long quotes using IQR
q1 = df["quote_length"].quantile(0.25)
q3 = df["quote_length"].quantile(0.75)
iqr = q3 - q1
upper = q3 + 1.5 * iqr
anomalies = df[df["quote_length"] > upper]
print("6. Potential long-quote anomalies:", len(anomalies))

df.to_csv("outputs/eda_enriched_quotes.csv", index=False)
print("\nSaved outputs/eda_enriched_quotes.csv")
