"""
CodeAlpha Data Analytics Internship - Task 1
Web Scraping: Quotes to Scrape

Run:
    pip install requests beautifulsoup4 pandas
    python src/task1_web_scraping.py
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = "https://quotes.toscrape.com/"
rows = []
url = BASE_URL

while url:
    response = requests.get(url, timeout=20)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    for item in soup.select("div.quote"):
        rows.append({
            "quote": item.select_one("span.text").get_text(strip=True),
            "author": item.select_one("small.author").get_text(strip=True),
            "tags": ", ".join(t.get_text(strip=True) for t in item.select("a.tag")),
        })

    next_link = soup.select_one("li.next a")
    url = BASE_URL.rstrip("/") + next_link["href"] if next_link else None

df = pd.DataFrame(rows)
df.to_csv("data/quotes_dataset.csv", index=False)
print(f"Saved {len(df)} quotes to data/quotes_dataset.csv")
