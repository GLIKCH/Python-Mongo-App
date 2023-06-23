# Joel De Alba
# Southern New Hampshire University
# 06/30/23
# Professor Dr. Tad Kellog

# Importing Mongo Client
from pymongo import MongoClient

# Other necessary inputs
from bson.objectid import ObjectId
from bson.json_util import dumps
from ipywidgets import IntSlider
from ipywidgets.embed import embed_minimal_html
from bson.objectid import ObjectId
import json


slider = IntSlider(value=40)
embed_minimal_html('export.html', views=[slider], title='Widgets export')

# Client Linking
client=MongoClient('mongodb://localhost:30122')
animal_data=client.AAC.animals.find({})

# AnimalShelter Class
class AnimalShelter(object):

    def __init__ (self, username, password):
        self.client = MongoClient('mongodb://%s:%s@127.0.0.1:30122/AAC' %(username, password))
        self.database = self.client['AAC']

    # Basic CRUD - Create Implementation
    def create (self, data):
        if data is not None:
            self.database.animals.insert_one(data)
            return True
        else: raise Exception("Nothing to save: data empty")

    # Basic CRUD - Read Implementation
    def read(self, search):
        if search is not None:
            if search:
                searchResult = self.database.animals.find(search)
                return searchResult
        else:
            exception = "Nothing to search, because search parameter is empty"
            return exception

    # Basic CRUD - Update Implementation
    def update(self, save):
        if save is not None:
            if save:
                saveResult = self.database.animals.insert_one(save)
                return saveResult
            else:
                exception = "Error: Nothing to Update"

    # Basic CRUD - Delete Implementation
    def delete(self, remove):
        if remove is not None:
            if remove:
                removeResult = self.database.animals.delete_one(remove)
            else:
                exception: "Error: Nothing to Delete"