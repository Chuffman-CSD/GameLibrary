#!/usr/bin/python3
#/Chris Huffman
#1/27/2020

import pickle
games = {}

game_num = 0

game_data = open("Database.pickle","rb")
games = pickle.load(game_data)
game_data.close()

def add_edit_game():
    global games
    global game_num
    print("\nRunning: add_edit_game()\n")
    print("""1.) Add Game
2.) Edit Game
3.) Back To Menu""")
    choice = input("Select a numerical option: ")
    if choice == "1":
        print("\nSelected: Adding Game.\n")
        genre = input("Genre: ").capitalize()
        title = input("Title: ").capitalize()
        if title in games:
            print("\nThe game is already in our database!\n")
        else:
            developer = input("Developer:").capitalize()
            publisher = input("Publsiher:").capitalize()
            system = input("Console:").capitalize()
            release_year = input("Release Year:").capitalize()
            personal_rating = input("Give it a rating from 1-10:")
            play_size = input("Select one, Multi/Single/Either:").capitalize()
            price = input("Price:")
            progress = input("Beat it? [Y]/[N]:").upper()
            year_bought = input("Year bought:").capitalize()
            game_num += 1
            games[game_num] = [genre,title,developer,publisher,system,release_year,personal_rating,play_size,price,progress,year_bought]
            data = open("Database.pickle","wb")
            pickle.dump(games,data)
            data.close()
            print("\nThe game ",title, "has been added!\n")
    elif choice == "2":
        pass
    elif choice == "3":
        print("\nLoading main manu!\n")

def print_all_games():
    global games
    global game_num
    print("\nRunning: print_all_games()\n")
    if games == {}:
        print("\nThere is no game data recorded.\n")
    else:
        key_list = list(games.keys())
        for game_num in key_list:
            print("----------")
            print("Genre: ",games[game_num][0])
            print("Title: ",games[game_num][1])
            print("Developer: ",games[game_num][2])
            print("Publisher: ",games[game_num][3])
            print("System: ",games[game_num][4])
            print("Release Year: ",games[game_num][5])
            print("Personal Rating: ",games[game_num][6])
            print("Multiplayer/Single Player/Either: ",games[game_num][7])
            print("Price Paid: ",games[game_num][8])
            print("Did you beat the game? [Y]/[N]: ",games[game_num][9])
            print("Year Bought: ",games[game_num][10])
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
                add_edit_game()
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
                games = pickle.dump(game_data)
                game_data.close()
            elif choice.isalpha():
                    print("\nAlphabetical Responses are prohibited.\n")
if __name__ == "__main__":
    mainMenu()
