"""
CodeAlpha Data Analytics Internship - Task 3
Data Visualization

Run:
    pip install pandas matplotlib
    python src/task3_visualization.py
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("outputs/charts", exist_ok=True)
df = pd.read_csv("outputs/eda_enriched_quotes.csv")

# 1. Quote word-count distribution
plt.figure(figsize=(9, 5))
plt.hist(df["word_count"], bins=15)
plt.title("Distribution of Quote Word Counts")
plt.xlabel("Words per Quote")
plt.ylabel("Number of Quotes")
plt.tight_layout()
plt.savefig("outputs/charts/01_word_count_distribution.png", dpi=160)
plt.close()

# 2. Top authors
top_authors = df["author"].value_counts().head(10).sort_values()
plt.figure(figsize=(9, 5))
plt.barh(top_authors.index, top_authors.values)
plt.title("Top 10 Authors by Number of Quotes")
plt.xlabel("Number of Quotes")
plt.tight_layout()
plt.savefig("outputs/charts/02_top_authors.png", dpi=160)
plt.close()

# 3. Top tags
tags = (
    df["tags"].fillna("")
    .str.split(", ")
    .explode()
    .replace("", pd.NA)
    .dropna()
    .value_counts()
    .head(10)
    .sort_values()
)
plt.figure(figsize=(9, 5))
plt.barh(tags.index, tags.values)
plt.title("Top 10 Quote Tags")
plt.xlabel("Number of Quotes")
plt.tight_layout()
plt.savefig("outputs/charts/03_top_tags.png", dpi=160)
plt.close()

# 4. Quote length vs word count
plt.figure(figsize=(8, 5))
plt.scatter(df["word_count"], df["quote_length"], alpha=0.65)
plt.title("Quote Length vs Word Count")
plt.xlabel("Word Count")
plt.ylabel("Character Count")
plt.tight_layout()
plt.savefig("outputs/charts/04_length_vs_words.png", dpi=160)
plt.close()

print("Charts saved in outputs/charts/")
