"""
This Python file contains the ranking dataframe and the list of countries.
"""

# Imports pandas to the file.
import pandas as pd

# Set display options for rows and columns
pd.set_option('display.max_rows', None)  # None means no limit
pd.set_option('display.max_columns', None)

# If you want to control the column width:
pd.set_option('display.max_colwidth', None)

# Imports the ranking csv file and converts it to be printed out.
ranking_2024 = pd.read_csv("csv_files/2024/ranking.csv").values.tolist()
# Imports the ranking csv file and converts it to be printed out.
countries_df = pd.read_csv("csv_files/2024/countries.csv").values.tolist()
# Imports the ranking csv file and converts it to be printed out.
years_df = pd.read_csv("csv_files/2024/years.csv").values.tolist()
# Imports the ranking csv file and converts it to be printed out.
ranking_1769_df = pd.read_csv("csv_files/2024/club1769.csv").values.tolist()
# List of countries is empty, but will be appended.
countries = []
# List of all the users.
users = {}

# Adds all the countries to the list of countries.
for row in ranking_2024:
    if row[7] not in countries:
        countries.append(row[7])
# Removes nan from the list, which is the first element.
countries.pop(0)

# Appends the dictionary containing the participating users and how many entries they ranked.
for k in range(17, len(ranking_2024[1])):
    us = ranking_2024[1][k]
    users[us] = int(ranking_2024[0][k])
