"""
This is the main program where the user will analyze the ranking sheet.
"""

# Imports the ranking and list of countries to this program.
from import_ranking import ranking_df, countries_df, years_df, ranking_1769_df, countries, users_1769, all_users

def entire_ranking(ranking=ranking_df):
    print("The Entire Ranking (All Users)")
    for n in range(4, len(ranking)):
        entry = ranking[n]
        print(f"{entry[0]}. {entry[7]} {entry[3]}: {entry[10]} - {entry[11]} - {entry[14]}")

def all_year_average(ranking=years_df):
    print("All Years Ranked by Averages")
    for n in range(len(ranking)):
        year = ranking[n]
        print(f"{year}")

# Main function containing the main program.
def main():
    # for i in range(4, 104):
    #     print(ranking_df[i])
    # print(countries)
    # print(len(countries))
    # Print statements
    print("Welcome to the Analyzer250!\n\n")
    print("What would you like to get from the ranking of ALTESC250 2024?\n")
    # Choices
    print("1 - List of the entire ranking.")
    print("2 - List of the entire ranking.")
    # Gets user input
    choice1 = input("Type in the number associated with the choice you want: ")
    # Ensures that the user enters the number listed in the choices
    while choice1 not in [str(c) for c in range(1, 15)]:
        print("That is not a number listed. Try a number listed!")
        print("Here are the choices again.\n")
        choice1 = input("Type in the number associated with the choice you want: ")
    # Else statement converts the choice into an int value.
    else:
        choice1 = int(choice1)
    # If statements that calls each function depending on the choice.
    if choice1 == 1:
        entire_ranking()
    elif choice1 == 2:
        all_year_average()

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