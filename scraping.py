import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO
import os

# List of URLs to scrape
urls = [
    f'https://www.swimrankings.net/index.php?page=meetDetail&meetId=626385&gender=1&styleId={i}' 
    for i in range(1, 20)
]

# Column names for DataFrame
column_names = ['Place', 'Name', 'Year of birth', 'Country code', 'Country', 'Time', 'Event']

def scrape_meet_results(url):
    """Scrape results from a given URL and return a list of DataFrames."""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    tables = soup.find_all('table', class_='meetResult')

    dataframes = []
    for table in tables:
        df = pd.read_html(StringIO(str(table)))[0].iloc[:, :-2]
        event = df.columns[0]
        df.columns = column_names[:-1]  # Exclude the 'Event' column for now
        df['Event'] = event
        dataframes.append(df)

    return dataframes

# Collect all results
all_dataframes = [df for url in urls for df in scrape_meet_results(url)]

# Combine DataFrames
result_df = pd.concat(all_dataframes, axis=0, ignore_index=True)

# Ensure the output directory exists
output_dir = 'results'
os.makedirs(output_dir, exist_ok=True)

# Save the result DataFrame to CSV
result_df.to_csv(os.path.join(output_dir, 'result_data.csv'), index=False)

# Display the first 5 rows of the DataFrame
print(result_df.head(5))
