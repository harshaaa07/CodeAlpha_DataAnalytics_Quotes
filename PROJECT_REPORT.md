# CodeAlpha Data Analytics Internship — Project Report

## 1. Objective
The objective is to demonstrate practical data analytics skills through data collection, exploration, and visualization.

## 2. Task 1 — Web Scraping
Python Requests and BeautifulSoup are used to collect quote text, author names, and tags from a public practice website. The scraper follows pagination and stores the resulting records in CSV format.

### Output
`data/quotes_dataset.csv`

## 3. Task 2 — Exploratory Data Analysis
The dataset is examined for:
- Number of records and columns
- Data types
- Missing values
- Duplicate records
- Quote length
- Word count
- Number of tags
- Most frequent authors
- Most frequent tags
- Potential unusually long quotes using an IQR-based rule

### Output
`outputs/eda_enriched_quotes.csv`

## 4. Task 3 — Data Visualization
Four visualizations are generated:
1. Distribution of quote word counts
2. Top 10 authors by quote count
3. Top 10 tags
4. Relationship between word count and character count

### Outputs
`outputs/charts/01_word_count_distribution.png`
`outputs/charts/02_top_authors.png`
`outputs/charts/03_top_tags.png`
`outputs/charts/04_length_vs_words.png`

## 5. Conclusion
The project demonstrates an end-to-end analytics workflow: collect data, inspect and enrich it, identify patterns/anomalies, and communicate findings visually.

The exact numerical findings are generated automatically after running the scraper and EDA scripts, so they remain tied to the collected dataset rather than being invented in advance.
