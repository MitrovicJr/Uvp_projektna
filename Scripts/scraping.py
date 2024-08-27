import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO
import os

#Saving the URL's of websites to scrape
urls = [
    f'https://www.swimrankings.net/index.php?page=meetDetail&meetId=626385&gender=1&styleId={i}' 
    for i in range(1, 20)
]

# Column names for each Dataframe
column_names = ['Place', 'Name', 'Year of birth', 'Country code', 'Country', 'Time', 'Event']

def scrape_meet_results(url):
    #Finds all relevant 'table' elements from the url and saves them into the 'tables' variable
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    tables = soup.find_all('table', class_='meetResult')

    #Saves the tables into a Pandas Dataframe and adds them to the list of dataframes
    dataframes = []
    for table in tables:
        df = pd.read_html(StringIO(str(table)))[0].iloc[:, :-2] #Excludes the last 2 columns, which are irrelevant for the analysis
        event = df.columns[0] #Extracts the event name
        df.columns = column_names[:-1]
        df['Event'] = event #Saves the event name into a new column
        dataframes.append(df)

    return dataframes

# Runs the relevant function on all saved URL's
all_dataframes = [df for url in urls for df in scrape_meet_results(url)]

# Concatenates the dataframes into one
result_df = pd.concat(all_dataframes, axis=0, ignore_index=True)

# Ensures the output directory exists
output_dir = 'results'
os.makedirs(output_dir, exist_ok=True)

# Saves the result DataFrame to a csv file
result_df.to_csv(os.path.join(output_dir, 'result_data.csv'), index=False)

# prints the first 5 elements of the concatenated dataframe, to check for abnormalities
print(result_df.head(5))
