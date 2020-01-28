#!/usr/bin/python3
#Chris Huffman
#1/28/2020

import pickle

games = {}

data = open("Database.pickle","wb")
pickle.dump(games,data)
data.close()
