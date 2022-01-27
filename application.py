from distutils.command.clean import clean
from multiprocessing.sharedctypes import Value
import constants
import copy
import os
from constants import PLAYERS, TEAMS
from copy import deepcopy



teams_copy = copy.deepcopy(TEAMS)
players_copy = copy.deepcopy(PLAYERS)

max_players = 6

panthers = []
bandits = []
warriors = []

def wipe_menu():
    os.system("cls" if os.name == "nt" else "clear")

def clean_data():
    for player in players_copy:
        if player.get("experience") == "NO":
            player ["height"] = int(player["height"][:2])
            player ["guardians"] = player["guardians"].split(" and ")
            player["experience"] = False

        else:
            player ["height"] = int(player["height"][:2])
            player ["guardians"] = player["guardians"].split(" and ")
            player["experience"] = True
    
clean_data()

def assign_team():
    count = 0

    for player in players_copy:
        if count < 6 and len(panthers) <= max_players:
            player["team"] = "Panthers"
            panthers.append(player)
            count += 1
        elif count < 12 and len(bandits) <= max_players:
            player["team"] = "Bandits"
            bandits.append(player)
            count += 1
        else:
            player["team"] = "Warriors"
            warriors.append(player)
            count += 1

assign_team()

def team_selection():
    print("\nWhich team would you like to view the stats for?")
    print("""\nPlease select an option:
    \n1) Panthers
    \n2) Bandits
    \n3) Warriors
    """)

    while True:
        try:

            command = input("Please select an option: ")

            if command == "1":
                wipe_menu()
                select_team_1(panthers)
                break
            elif command == "2":
                wipe_menu()
                select_team_2(bandits)
                break
            elif command == "3":
                wipe_menu()
                select_team_3(warriors)
            elif command > "3":
                print("\nPlease enter a valid selection")
            elif command < "1":
                    print("\nPlease enter a valid selection")
        except KeyError:
            print("\nPlease enter a valid selection ")

def exit():
    print("\n\n\nThank you for using our service, please check back soon!\n")
    exit

def select_team_1(panthers):
    wipe_menu()
    num_players = len(panthers)
    num_exper = []
    num_inexper = []
    height = []
    names = []
    guardians = []
    team_name_panthers = TEAMS[0]
    

    for key in panthers:
        if key["experience"] == True:
            num_exper.append(key)
        else:
            num_inexper.append(key)

    for key in panthers:
        height.append(key["height"])
        
    for key in panthers:
        names.append(key["name"])


    for key in panthers:
        guardians.append(key["guardians"])

    sum_height = sum(height)
    avg_height = round(sum_height / 6, 2)
    
    print("*" * 60)
    print(f"Team Name: {team_name_panthers}")
    print(f"There are {num_players} players on the team")
    print(f"There are {len(num_exper)} experienced players and {len(num_inexper)} inexperienced players")
    print(f"The average height on the team is: {avg_height}")
    print(f"\nThe names of the players are: {names}")
    print(f"The guardians on the players are: {guardians}\n\n")

    print("""
    Please select an option:
    \n1) View Other Team Stats
    \n2) Exit
    """)

    while True:
        try:

            command = input("Please select an option: ")

            if command == "1":
                wipe_menu()
                team_selection()
                break
            elif command == "2":
                wipe_menu()
                exit()
                break
            elif command > "2":
                print("\nPlease enter a valid selection")
            elif command < "1":
                print("\nPlease enter a valid selection")
        except KeyError:
            print("\nPlease enter a valid selection ")



def select_team_2(bandits):
    wipe_menu()
    num_players = len(bandits)
    num_exper = []
    num_inexper = []
    height = []
    names = []
    guardians = []
    team_name_bandits = TEAMS[1]

    for key in bandits:
        if key["experience"] == True:
            num_exper.append(key)
        else:
            num_inexper.append(key)

    for key in bandits:
        height.append(key["height"])
        
    for key in bandits:
        names.append(key["name"])

    for key in bandits:
        guardians.append(key["guardians"])

    sum_height = sum(height)
    avg_height = round(sum_height / 6, 2)

    
    print("*" * 60)
    print(f"Team: {team_name_bandits}")
    print(f"\nThere are {num_players} players on the team")
    print(f"There are {len(num_exper)} experienced players and {len(num_inexper)} inexperienced players")
    print(f"The average height on the team is: {avg_height}")
    print(f"\nThe names of the players are: {names}")
    print(f"The guardians on the players are: {guardians}\n\n")

    print("""
    Please select an option:
    \n1) View Other Team Stats
    \n2) Exit
    """)

    while True:
        try:

            command = input("Please select an option: ")

            if command == "1":
                wipe_menu()
                team_selection()
                break
            elif command == "2":
                wipe_menu()
                exit()
                break
            elif command > "2":
                print("\nPlease enter a valid selection")
            elif command < "1":
                print("\nPlease enter a valid selection")
        except KeyError:
            print("\nPlease enter a valid selection ")

def select_team_3(warriors):
    wipe_menu()
    num_players = len(warriors)
    num_exper = []
    num_inexper = []
    height = []
    names = []
    guardians = []
    team_name_warriors = TEAMS[2]

    for key in warriors:
        if key["experience"] == True:
            num_exper.append(key)
        else:
            num_inexper.append(key)

    for key in warriors:
        height.append(key["height"])
        
    for key in warriors:
        names.append(key["name"])

    for key in warriors:
        guardians.append(key["guardians"])

    sum_height = sum(height)
    avg_height = round(sum_height / 6, 2)

    
    print("*" * 60)
    print(f"Team: {team_name_warriors}")
    print(f"\nThere are {num_players} players on the team")
    print(f"There are {len(num_exper)} experienced players and {len(num_inexper)} inexperienced players")
    print(f"The average height on the team is: {avg_height}")
    print(f"\nThe names of the players are: {names}")
    print(f"The guardians on the players are: {guardians}\n\n")

    print("""
    Please select an option:
    \n1) View Other Team Stats
    \n2) Exit
    """)

    while True:
        try:

            command = input("Please select an option: ")

            if command == "1":
                wipe_menu()
                team_selection()
                break
            elif command == "2":
                wipe_menu()
                exit()
                break
            elif command > "2":
                print("\nPlease enter a valid selection")
            elif command < "1":
                print("\nPlease enter a valid selection")
        except KeyError:
            print("\nPlease enter a valid selection ")

def main():
    print(
    """
    ****************************************************************************************************
    ***********************    Welcome to the basketball team viewer     *******************************
    ****************************************************************************************************
    """
    )
    print("""
    Please select an option:
    \n1) View Team Stats
    \n2) Exit
    """)

    while True:
        try:

            command = input("Please select an option: ")

            if command == "1":
                wipe_menu()
                team_selection()
                break
            elif command == "2":
                wipe_menu()
                exit()
                break
            elif command > "2":
                print("\nPlease enter a valid selection")
            elif command < "1":
                print("\nPlease enter a valid selection")
        except KeyError:
            print("\nPlease enter a valid selection ")


if __name__ == "__main__":
    main()



