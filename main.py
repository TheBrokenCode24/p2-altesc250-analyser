"""
This is the main program where the user will analyze the ranking sheet.
"""

# Imports the ranking and list of countries to this program.
from import_ranking import ranking_df, countries_df, years_df, ranking_1769_df, countries, users_1769, all_users


# Main function containing the main program.
def main():
    # for i in range(4, 104):
    #     print(ranking_df[i])
    # print(countries)
    # print(len(countries))
    print("Welcome to the Analyzer250!\n\n")
    print("What would you like to get from the ranking of ALTESC250 2024?")
    print("1. List of the entire ranking.")
    print(users_1769)
    print(all_users)
    # 1. List of the entire ranking. (ranking.csv)
    # 2. List of the entire ranking from those who ranked all the songs (club_1769.csv).
    # 3. List of the entire ranking from a specific user (ranking.csv).
    # 4. All years ranked by average.
    # 5. All years ranked by average from those who ranked all the songs.
    # 6. All years ranked by average of a specific user.
    # 7. All the countries ranked by average.
    # 8. All the countries ranked by average from those who ranked all the songs.
    # 9. All the countries ranked by average of a specific user.
    # 10. All the entries from a specific year ranked.
    # 11. All the entries from a specific year ranked from those who ranked all the songs.
    # 12. All the entries from a specific year ranked from a specific user.
    # 13. All the entries from a specific country ranked.
    # 14. All the entries from a specific country ranked from those who ranked all the songs.
    # 15. All the entries from a specific country ranked from a specific user.
    
# This runs the main program.
if __name__ == "__main__":
    main()