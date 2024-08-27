The repository contains the project for my course 'Uvod v Programiranje'.
In the repository there is a python document, which contains the program for the web-scraping part of the project. The results of this project are stored in the 'results' folder, which contains a csv file.
Additionally, there is a Jupyter notebook which uses the data from the csv file and contains the data visualization and analysis for the project.

The goal of the project was to scrape the data from a swimming results website, and do some exploratory data analysis and visualization of the resulting data. The swimming data in question was the Tokyo 2020 olympics as the olympics are regarded as the top of the top of the sport of swimming.

The python script uses the bs4 and requests library to extract relevant tables and save them to a concatenated Dataframe using Pandas. The resulting dataframe is then stored as a csv file to be used in the jupyter notebook. It should also be noted that csv is perhaps not the most suitable format for saving the data, methods like parquet and croissant might be more efficient, but due to the relatively small size of the data this should not make a big difference.

The Jupyter notebook has a few different angles and perspectives on the data, from analysis of the swimmers age to the relative success of the countries at the olympics. The Visualization libraries used are Matplotlib and Seaborn, with some Pandas needed for the analysis.