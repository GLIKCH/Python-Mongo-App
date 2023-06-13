# Joel De Alba
# Southern New Hampshire University
# 06/30/23
# Professor Dr. Tad Kellog

import Script
scr = Script
# Importing Mongo Client
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30122
        DB = 'AAC'
        COL = 'animals'

        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    def read(self, search):
        search = input("Search Query: ")
        # Checks to see if the data is null or empty and returns exception in either case
        if search is not None:
            if search:
                searchResult = self.database.animals.find(search)
                print("Search was Successful!")
                return searchResult
        else:
            print("Nothing to search, because search parameter is empty")
            return scr

    def create(self, data):
        data = input("What collection would you like to create? Be sure to use MongoDB syntax\n --| ")
        # Checks to see if the data is null or empty and returns false in either case
        if data is None:
            self.database.animals.insert_one(data)
            print("Created Successfully!")
            return scr
        else:
            print("Error: Not Created")
            return scr

    def update(self, modify):
        modify = input("What collection would you like to update?\n --|")
        # Checks if data is present, if not then updates the collection
        if modify is not None:
            self.database.animals.update_one(modify)
            print("Updated Successfully!")
            return scr
        else:
            updRequest = input("Entry not found, Would you like to create a new collection? Y / N ---- " + modify + "\n\n--| ")
            if updRequest is "y" or "Y":
                self.database.animals.insert_one(modify)
                print("Created Successfully!")
                return scr
            if updRequest is "n" or "N":
                print("No collection was created.")
                return scr

    def delete(self, remove):
        remove = input("What collection would you like to delete? \n--| ")
        if remove is not None:
            self.database.animals.delete(remove)
            print("Deleted Successfully!")
            return scr
        else:
            print("No Entry Found!")
            return scr
