"""
This is the main program where the user will analyze the ranking sheet.
"""

# Imports the ranking and list of countries to this program.
from import_ranking import ranking_df, countries_df, years_df, ranking_1769_df, countries, users_1769, all_users

# Function prints out the entire ranking based on averages from all users.
def entire_ranking(ranking=ranking_df):
    print("\nThe Entire Ranking (All Users):")
    for n in range(4, len(ranking)):
        entry = ranking[n]
        print(f"{entry[0]}. {entry[7]} {entry[3]}: {entry[10]} - {entry[11]} - {entry[14]}")

# Function prints out the entire ranking based on averages of all users who ranked all songs.
def entire_ranking_1769(ranking=ranking_1769_df):
    print("\nThe Entire Ranking (1769 Club):")
    for n in range(4, len(ranking)):
        entry = ranking[n]
        print(f"{entry[1]}. {entry[8]} {entry[4]}: {entry[11]} - {entry[12]} - {entry[15]}")

# Function prints out the averages of each year.
def all_year_average(ranking=years_df):
    print("All Years Ranked by Averages")
    for n in range(len(ranking)):
        year = ranking[n]
        print(f"{year[0]}. {year[1]} - {year[2]}")

# Function prints out the averages of each country.
def all_country_average(ranking=countries_df):
    print("All Countries Ranked by Averages")
    for n in range(len(ranking)):
        country = ranking[n]
        print(f"{country[0]}. {country[2]} - {country[3]}")

# Main function containing the main program.
def main():
    # Print statements
    print("Welcome to the Analyzer250!\n\n")
    print("What would you like to get from the ranking of ALTESC250 2024?\n")
    
    # Choices
    # 1. List of the entire ranking. (ranking.csv)
    # 2. List of the entire ranking from those who ranked all the songs (club_1769.csv).
    # 3. List of the entire ranking from a specific user (ranking.csv).
    print("1 - List of the entire ranking.")
    # 4. All years ranked by average.
    # 5. All years ranked by average from those who ranked all the songs.
    # 6. All years ranked by average of a specific user.
    print("2 - All the years ranked by average.")
    # 7. All the countries ranked by average.
    # 8. All the countries ranked by average from those who ranked all the songs.
    # 9. All the countries ranked by average of a specific user.
    print("3 - All the countries ranked by average.")
    # 10. All the entries from a specific year ranked.
    # 11. All the entries from a specific year ranked from those who ranked all the songs.
    # 12. All the entries from a specific year ranked from a specific user.
    print("4 - All the entries from a specific year ranked.")
    # 13. All the entries from a specific country ranked.
    # 14. All the entries from a specific country ranked from those who ranked all the songs.
    # 15. All the entries from a specific country ranked from a specific user.
    print("5 - All the entries from a specific country ranked.")
    
    # Gets user input
    choice1 = input("Type in the number associated with the choice you want: ")
    
    # Ensures that the user enters the number listed in the choices
    while choice1 not in [str(c) for c in range(1, 6)]:
        print("That is not a number listed. Try a number listed!")
        print("Here are the choices again.\n")
        choice1 = input("Type in the number associated with the choice you want: ")
    # Else statement converts the choice into an int value.
    else:
        choice1 = int(choice1)
    
    # If statements that calls each function depending on the choice.
    if choice1 == 1:
        print("\nWhere would you like to get the ranking from?")
        print("1 - All users")
        print("2 - All users who ranked all 1769 songs")
        print("3 - A specific user")

        # Gets user input
        choice2 = input("Type in the number associated with the choice you want: ")
        
        # Ensures that the user enters the number listed in the choices
        while choice2 not in [str(c) for c in range(1, 4)]:
            print("That is not a number listed. Try a number listed!")
            print("Here are the choices again.\n")
            choice2 = input("Type in the number associated with the choice you want: ")
        # Else statement converts the choice into an int value.
        else:
            choice2 = int(choice2)

        if choice2 == 1:
            entire_ranking()
        elif choice2 == 2:
            entire_ranking_1769()
        else:
            pass
    elif choice1 == 2:
        all_year_average()
    elif choice1 == 3:
        all_country_average()
    elif choice1 == 4:
        pass

    
# This runs the main program.
if __name__ == "__main__":
    main()