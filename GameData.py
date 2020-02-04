#!/usr/bin/python3
#/Chris Huffman
#1/27/2020

import pickle
games = {}

key = 0

unknown_entries_special = ["!","?","'","@","#","$","%","^","&","*","(",")","-","_","=","+","\\",'"',"{","}","[","]",":",";","/",".",">","<","~","`"]

game_data = open("Database.pickle","rb")
games = pickle.load(game_data)
game_data.close()

saved = 0
changed = 0

def add_edit_game():
    global games
    global key
    print("\nRunning: add_edit_game()\n")
    print("""===============
 Add/Edit Menu
===============
| 1.) Add Game
| 2.) Edit Game
| 3.) Back To Menu\n""")
    choice = input("Select a numerical option: ")
    if choice == "1":
        print("\n=================")
        print("Add Menu Selected")
        print("=================")
        genre = input("| Genre: ").capitalize()
        title = input("| Title: ").capitalize()
        if title in games:
            print("\nThe game is already in our database!\n")
        else:
            developer = input("| Developer:").capitalize()
            publisher = input("| Publsiher:").capitalize()
            system = input("| Console:").capitalize()
            release_year = input("| Release Year:").capitalize()
            personal_rating = input("| Give it a rating from 1-10:")
            play_size = input("| Select one, Multi/Single/Either:").capitalize()
            price = input("| Price:")
            progress = input("| Beat it? [Y]/[N]:").upper()
            year_bought = input("| Year bought:").capitalize()
            key += 1
            for key in games:
                key += 1
            games[key] = [genre,title,developer,publisher,system,release_year,personal_rating,play_size,price,progress,year_bought]
            data = open("Database.pickle","wb")
            pickle.dump(games,data)
            data.close()
            print("\nThe game ",title, "has been added!\n")
    elif choice == "2":
        for key in games.keys():
            print(key,"-",games[key][1])
        if key == 0:
            print("\n***There are is no game data.***")
        else:
            edit_key = int(input("Which game would you like to edit: "))
            print("""========================
Select an option to edit
========================
| 1.) Genre
| 2.) Title
| 3.) Developer
| 4.) Publisher
| 5.) Console
| 6.) Release Year
| 7.) Personal Rating
| 8.) Player Compatibilty
| 9.) Price
| 10.) Beat it?
| 11.) Year Bought
| 12.) Edit All Information
| 13.) Cancel""")
            choice = input("Select an option")
            if choice.isdigit():
                if choice == "1":
                    genre = input("Enter the genre: ")
                    print("Genre changed from",games[key][0],"to",genre,".")
                    changed += 1
                    saved = 0
                    games[key][0] = genre
                if choice == "2":
                    title = input("Enter the title: ")
                    print("Title changed from",games[key][1],"to",title,".")
                    changed += 1
                    saved = 0
                    games[key][1] = title
                if choice == "3":
                    developer = input("Enter the developer: ")
                    print("Developer changed from",games[key][2],"to",developer,".")
                    changed += 1
                    saved = 0
                    games[key][2] = developer
                if choice == "4":
                    publisher = input("Enter the publisher: ")
                    print("Publisher changed from",games[key][3],"to",publisher,".")
                    changed += 1
                    saved = 0
                    games[key][3] = publisher
                if choice == "5":
                    console = input("Enter the console: ")
                    print("Console changed from",games[key][4],"to",console,".")
                    changed += 1
                    saved = 0
                    games[key][4] = console
                if choice == "6":
                    release_year = input("Enter the release year: ")
                    print("Release year changed from",games[key][5],"to",release_year,".")
                    changed += 1
                    saved = 0
                    games[key][5] = release_year
                if choice == "7":
                    personal_rating = input("Enter the personal rating: ")
                    print("Personal rating changed from",games[key][6],"to",personal_rating,".")
                    changed += 1
                    saved = 0
                    games[key][6] = personal_rating
                if choice == "8":
                    compatibility = input("Enter the player compatibility: ")
                    print("compatibility changed from",games[key][7],"to",compatibility,".")
                    changed += 1
                    saved = 0
                    games[key][7] = compatibility
                if choice == "9":
                    price = input("Enter the player compatibility: ")
                    print("Price changed from",games[key][8],"to",price,".")
                    changed += 1
                    saved = 0
                    games[key][8] = price
                if choice == "10":
                    progress = input("Enter the player compatibility: ")
                    print("Beat it changed from",games[key][9],"to",progress,".")
                    changed += 1
                    saved = 0
                    games[key][9] = progress
                if choice == "11":
                    year_bought = input("Enter the player compatibility: ")
                    print("Purchase year changed from",games[key][9],"to",year_bought,".")
                    changed += 1
                    saved = 0
                    games[key][9] = year_bought
                if choice == "12":
                    genre = input("Enter the genre: ")
                    print("\nGenre changed from",games[key][0],"to",genre,".")
                    games[key][0] = genre
                    title = input("Enter the title: ")
                    print("\nTitle changed from",games[key][1],"to",title,".")
                    games[key][1] = title
                    developer = input("Enter the developer: ")
                    print("\nDeveloper changed from",games[key][2],"to",developer,".")
                    games[key][2] = developer
                    publisher = input("Enter the publisher: ")
                    print("\nPublisher changed from",games[key][3],"to",publisher,".")
                    games[key][3] = publisher
                    console = input("Enter the console: ")
                    print("\nConsole changed from",games[key][4],"to",console,".")
                    games[key][4] = console
                    release_year = input("Enter the release year: ")
                    print("\nRelease year changed from",games[key][5],"to",release_year,".")
                    games[key][5] = release_year
                    personal_rating = input("Enter the personal rating: ")
                    print("\nPersonal rating changed from",games[key][6],"to",personal_rating,".")
                    games[key][6] = personal_rating
                    compatibility = input("Enter the player compatibility: ")
                    print("\nCompatibility changed from",games[key][7],"to",compatibility,".")
                    games[key][7] = compatibility
                    price = input("Enter the player compatibility: ")
                    print("\nPrice changed from",games[key][8],"to",price,".")
                    games[key][8] = price
                    progress = input("Enter the player compatibility: ")
                    print("\nBeat it changed from",games[key][9],"to",progress,".")
                    games[key][9] = progress
                    year_bought = input("Enter the player compatibility: ")
                    print("\nPurchase year changed from",games[key][9],"to",year_bought,".")
                    changed += 1
                    saved = 0
                    games[key][9] = year_bought
                if choice == "13":
                    print("\n***Cancelling!***\n")
            elif choice.isalpha():
                print("\n***Invalid response. [",choice,"]***")
    elif choice in unknown_entries_special:
        print("\n***Invalid character. [",choice,"]***")
    elif choice == "3":
        print("\nLoading main manu!\n")

def print_all_games():
    global games
    global key
    print("\nRunning: print_all_games()\n")
    if games == {}:
        key = 0
        print("\nThere is no game data recorded.\n")
    else:
        key_list = list(games.keys())
        for key in key_list:
            print("----------")
            print("| Genre: ",games[key][0])
            print("| Title: ",games[key][1])
            print("| Developer: ",games[key][2])
            print("| Publisher: ",games[key][3])
            print("| System: ",games[key][4])
            print("| Release Year: ",games[key][5])
            print("| Personal Rating: ",games[key][6])
            print("| Multiplayer/Single Player/Either: ",games[key][7])
            print("| Price Paid: ",games[key][8])
            print("| Did you beat the game? [Y]/[N]: ",games[key][9])
            print("| Year Bought: ",games[key][10])
            print("----------")
        key = len(games)
        print("\nThere are",key,"games in the database!\n")

def search_by_title():
    tally = 0
    print("\nRunning: serch_by_title(()\n")
    title = input("Title you wish to search: ").capitalize()
    for key in games.keys():
        entry = games[key]
        if title in entry[1]:
            tally += 1
            print("\n",tally,".)",entry[1])
   

def remove_a_game():
    global key
    global saved
    global changed
    for key in games.keys():
        print(key)
        print("\n",key,"-",games[key][1],"\n")
        if key == 0:
            print("\n***There is no game data.***")
    if games == {}:
        print("\n***There is no game data.***")
    else:
        edit_key = int(input("Which game would you like to remove: "))
        if edit_key in games:
            print("\nRemoving: ",games[edit_key][1],"from the database..\n")
            print("***",games[edit_key][1],"has been removed!***")
            games.pop(edit_key)
            changed += 1
            saved = 0
            key = len(games)
            print("\nThere are now",key,"games in the database!\n")
            
        elif edit_key > len(games):
            print("\n",edit_key,"is not a valid option!\n")
            edit_key = None    
            if edit_key == None:
                edit_key = 0
                print("\n")
            
        else:
            print("\n",edit_key,"is not a valid option!\n")
            edit_key = None    
            if edit_key == None:
                edit_key = 0
                print("\n")
    
def save_database():
    saved += 1
    print("\n***Successfully saved the current database!***\n")
    game_data = open("Database.pickle","wb")
    pickle.dump(games,game_data)
    game_data.close()
    if saved == 0 and changed == 0:
        saved = 0
        changed = 0
    elif saved == 0 and changed >= 1:
        saved = 1
        changed = 0

def mainMenu():
    global changed
    global games
    global saved
    global unknown_entries_special
    while True:
        print("""
========================
    GameLibrary .Inc
========================

---MAIN MANU---
| 1.) Add/Edit Game
| 2.) Print All Games
| 3.) Search Game By Title
| 4.) Remove a Game
| 5.) Save Database

| 6.) Quit\n""")
        choice = input("Select a numerical option: ").lower()
        if choice.isdigit():
            if choice == "1":
                add_edit_game()
            elif choice == "2":
                print_all_games()
            elif choice == "3":
                search_by_title()
            elif choice == "4":
                remove_a_game()
            elif choice == "5":
                if saved == 0:
                    print("\n***The current database has no changes to be saved.***\n")
                    choice = input("Save anyways? [Y]/[N]: ").upper()
                    if choice == "Y":
                        print("\n*Database Saved.*\n")
                    elif choice == "N":
                        print("\n*Loading Main Menu.*\n")
                else:
                    save_database()
            elif choice == "6":
                if saved == 0 and changed == 0:
                    print("\nGoodbye!\n")
                    exit()
                elif saved == 0 and changed >= 1:
                    x = 0
                    while x == 0:
                        choice = input("Woah there, you never saved! Do you wish to save? [Y]/[N]: ").upper()
                        if choice == "Y":
                            x = 1
                            data = open("Database.pickle","wb")
                            pickle.dump(games,data)
                            data.close()
                            print("\n***Saved!***\n")
                        elif choice == "N":
                            x = 1
                            print("\n***Not saved!***\n")
                            exit()
                        else:
                            print("\n***",choice,"is not a valid response!***\n")
                elif saved == 1 and changed >= 1:
                    print("\nGoodbye!\n")
                    exit()
        elif choice.isalpha():
            print("\n***Invalid character. [",choice,"]***")
        elif choice in unknown_entries_special:
            print("\n***Invalid character. [",choice,"]***")
if __name__ == "__main__":
    mainMenu()
