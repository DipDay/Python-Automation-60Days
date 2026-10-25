from io import StringIO
import pandas as pd
import requests

url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
response.raise_for_status()

# Wrap in StringIO to avoid OSError/deprecation warnings in pandas 2.x
dfs = pd.read_html(StringIO(response.text))

# Index 0 is the main population table
df = dfs[0]
print(df)
