#!/usr/bin/python3
#/Chris Huffman
#1/27/2020

def add_edit_game():
    print("\nRunning: add_edit_game()\n")
    mainMenu()

def print_all_games():
    print("\nRunning: print_all_games()\n")
    mainMenu()

def search_by_title():
    print("\nRunning: serch_by_title(()\n")
    mainMenu()

def remove_a_game():
    print("\nRunning: remove_a_game()\n")
    mainMenu()

def save_database():
    print("\nRunning: save_database()\n")
    mainMenu()

def quit_program():
    print("\nRunning: quit_program()\n")
    mainMenu()

def mainMenu():
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
    x = 0
    while x == 0:
        choice = input("Select a numerical option: ")
        if choice.isdigit():
            if choice == "1":
                x = 1
                print_all_games()
            elif choice == "2":
                x = 1
                print_all_games()
            elif choice == "3":
                x = 1
                search_by_title()
            elif choice == "4":
                x = 1
                remove_a_game()
            elif choice == "5":
                x = 1
                quit_program()
            else:
                print("\n")
        elif choice.isalpha():
            print("\nAlphabetical Responses are prohibited.\n")
if __name__ == "__main__":
    mainMenu()
