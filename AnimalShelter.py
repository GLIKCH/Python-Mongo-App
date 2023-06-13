# Joel De Alba
# Southern New Hampshire University
# 06/30/23
# Professor Dr. Tad Kellog

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

    def create(self, data):
        # Checks to see if the data is null or empty and returns false in either case
        if data is not None:
            if data:
                self.database.animals.insert_one(data)
                print("Create Complete!")
                return True
        else:
            return False

    def read(self, search):
        # Checks to see if the data is null or empty and returns exception in either case
        if search is not None:
            if search:
                searchResult = self.database.animals.find(search)
                print("Search was Successful!")
                return searchResult
        else:
            exception = "Nothing to search, because search parameter is empty"
            return exception

    def update(self, modify):
        # Checks if data is present, if not then updates the collection
        if modify is not None:
            self.database.animals.update_one(modify)
            print("Updated Successfully!")

    def delete(self, remove):
        # Checks if entry exists, if not then deletes found collection
        if remove is not None:
            self.database.animals.delete(remove)