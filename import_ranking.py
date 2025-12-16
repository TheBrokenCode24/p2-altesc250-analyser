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
ranking_df = pd.read_csv("ranking.csv").values.tolist()
# Imports the ranking csv file and converts it to be printed out.
countries_df = pd.read_csv("countries.csv").values.tolist()
# Imports the ranking csv file and converts it to be printed out.
years_df = pd.read_csv("years.csv").values.tolist()
# Imports the ranking csv file and converts it to be printed out.
ranking_1769_df = pd.read_csv("club_1769.csv").values.tolist()
# List of countries is empty, but will be appended.
countries = []
# List of the users who ranked all the songs.
users_1769 = {}
# List of the users who didn't rank all the songs.
all_users = {}

# Adds all the countries to the list of countries.
for row in ranking_df:
    if row[7] not in countries:
        countries.append(row[7])
# Removes nan from the list, which is the first element.
countries.pop(0)

# Appends the dictionary containing the participating users and how many entries they ranked.
for k in range(17, len(ranking_1769_df[1])):
    user = ranking_1769_df[1][k]
    users_1769[user] = 1769

for m in range(17, len(ranking_df[1])):
    if ranking_df[0][m] == "1769":
        continue
    user2 = ranking_df[1][m]
    all_users[user2] = ranking_df[0][m]
