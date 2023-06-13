# Python-Mongo-App
CS-340 Client/Server Development - Project One Submission

# CRUD Python

CRUD Python is database development project that provides end users the ability to Create, Read, Update, and Delete MongoDB databases defined and constructed to be customizable for use with various different platforms.

##
## Installation

Any database that is created can be implemented within the development code and be used as csv or table format, a good visual example of this type of table database is Microsoft Excel.

Databases can be imported using

##
```bash
mongoimport --username="${MONGO_USER}" --password="${MONGO_PASS}" --port="${MONGO_PORT}" --host="${MONGO_HOST}" --collection animal --authenticationDatabase admin --file / CVS_DIRECTORY_HERE --type csv --headerline --db AAC
``` 
##

## Utilization Details

Once the database has been imported to MongoDB, the following commands can be executed to ensure the database is found within the list of databases:

##
```bash
mongosh
show dbs
use aac
show collections
```

> MongoSH - initializes the MongoDB shell to run mongo database queries and manage collections.

> Show DBS - Displays available database tables.

> use db - Loads and Utilizes the database of choice by name.

> Show Collections - Displays collection data entries.
##

## Implementing MongoDB within Python

First, Python must be installed, preferably versions above 3.0. Once Python is installed, all dependencies must be installed. The following line will install what is needed:

##
```bash
python3 -m pip install "pymongo[gssapi,aws,ocsp,snappy,zstd,encryption]"
```
##

This type of command runs on basic bash from Linux terminal.

## Script Implementation

The script was created utilizing PyCharm and Jupyter Notebook. The main script handles the CRUD  commands to input and edit collections within the database, while the AnimalShelter.ipynb handles the authentication and connection to the MongoDB server.

The class begins as follows:

##
```python
from pymongo import MongoClient
from bson.objectid import ObjectId
```
##

These are some necessary imports in order to create a successful class that can authenticate and connect to the database.

## Database Authentication Details

The variable data displayed below is to be replaced by the correct values related to the database the developer has imported. The data should be placed within the main database class file after the object class is implemented.
##

```python
class AnimalShelter(object):

def __init__(self):
    USER = 'admin_user_here'
    PASS = 'admin_user_password_here'
    HOST = 'Host_URI_here'
    PORT =  88888
    DB =   'database_name_here'
    COL =  'collection_here'

# Initialize Connection
self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
self.database = self.client['%s' % (DB)]
self.collection = self.database['%s' % (COL)]
```

##
Once the connection settings are set the rest of the python application can be developed in main.ipynb through Jupyter Notebook or through a Python IDE like PyCharm. Some examples of CRUD MongoDB are developed as such:
##

```python
database_here = database_class()

# If no data found, insert new collection
def create(self, data):
        if data is not None:
		    self.database.collection_here.insert_one(data)  # data should be dictionary            
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Read new entry
read = database_here.read( {"type":"collection_type"}  )
for collection_name in collection_group_name:
    print(collection_name)
```
##

We hope this project is beneficial for all developers looking to develop a python application with MongoDB database.
