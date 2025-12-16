# Imports pandas to the file.
import pandas as pd

# Set display options for rows and columns
pd.set_option('display.max_rows', None)  # None means no limit
pd.set_option('display.max_columns', None)

# If you want to control the column width:
pd.set_option('display.max_colwidth', None)

# Imports the ranking csv file and converts it to be printed out.
ranking_df = pd.read_csv("ranking.csv").values.tolist()
countries = []

for row in ranking_df:
    if row[7] not in countries:
        countries.append(row[7])

countries.pop(0)