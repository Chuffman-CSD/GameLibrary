#!/usr/bin/python3
#/Chris Huffman
#1/27/2020

def add_edit_game():
    print("\nRunning: add_edit_game()\n")

def print_all_games():
    print("\nRunning: print_all_games()\n")

def search_by_title():
    print("\nRunning: serch_by_title(()\n")

def remove_a_game():
    print("\nRunning: remove_a_game()\n")

def save_database():
    print("\nRunning: save_database()\n")

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

Q) Quit\n""")
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
                exit()
            elif choice.isalpha():
                    print("\nAlphabetical Responses are prohibited.\n")
if __name__ == "__main__":
    mainMenu()
