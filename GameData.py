#!/usr/bin/python3
#/Chris Huffman
#1/27/2020

import pickle

#games = {1:['FPS','HALO 3','Bungee','Microsoft','Xbox 360','2007','Either','either','30.00','Yes','1/15/2008'],2:['Action RPG','Grand Theft Auto V','Rockstar Games','Sony','Playstation 4','2013','Single PLayer','either','150.00','Yes','October 2, 2016']} #- Used this for debugging
games = {}

game_data = open("Database.pickle","rb")
games = pickle.load(game_data)
game_data.close()

def add_edit_game():
    print("\nRunning: add_edit_game()\n")

def print_all_games():
    print("\nRunning: print_all_games()\n")
    if games == {}:
        print("\nThere is no game data recorded.\n")
    else:
        key_list = list(games.keys())
        for game in key_list:
            print("----------")
            print("Genre: ",games[game][0])
            print("Title: ",games[game][1])
            print("Developer: ",games[game][2])
            print("Publisher: ",games[game][3])
            print("System: ",games[game][4])
            print("Release Year: ",games[game][5])
            print("Multiplayer/Single Player/Either: ",games[game][6])
            print("Price Paid: ",games[game][7])
            print("Year Bought: ",games[game][8])
            print("----------")

def search_by_title():
    print("\nRunning: serch_by_title(()\n")

def remove_a_game():
    print("\nRunning: remove_a_game()\n")

def save_database():
    print("\nRunning: save_database()\n")
    game_data = open("Database.pickle","wb")
    pickle.dump(games,game_data)
    game_data.close()

def mainMenu():
    while True:
        print("""
========================
    GameLibrary .Inc
========================

---MAIN MANU---
1.) Add/Edit Game
2.) Print All Games
3.) Search Game By Title
4.) Remove a Game
5.) Save Database

6) Quit\n""")
        choice = input("Select a numerical option: ")
        if choice.isdigit():
            if choice == "1":
                print_all_games()
            elif choice == "2":
                print_all_games()
            elif choice == "3":
                search_by_title()
            elif choice == "4":
                remove_a_game()
            elif choice == "5":
                save_database()
            elif choice == "6":
                exit()
            elif choice.isalpha():
                    print("\nAlphabetical Responses are prohibited.\n")
if __name__ == "__main__":
    mainMenu()
