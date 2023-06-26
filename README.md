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

The script was created utilizing PyCharm and Jupyter Notebook. The main script handles the commands to input and edit collections within the database from the AnimalShelter.py of which handles the authentication and connection to the MongoDB server. All of the CRUD functions are developed within the AnimalShelter.py.

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


Here is an image on the example utilized to manage CRUD functions and make updates to the MongoDB server database.
##

![image](https://github.com/GLIKCH/Python-Mongo-App/assets/53536316/f4c8b9b1-c963-48ce-9175-2b3baa670256)'

##

# Additional Final Module Edits
##

How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?

Maintainable, Readable, and Adaptable programs are implemented by understanding first and foremost the functionality, the syntax, the database connections made such as username, password, port, host, etc. Secondly once the terminology, syntax, and prerequizites are covered in regards to database document handling, import, and detection of the database table by query into mongosh for MongoDB database the rest of the development process relies on implementing code that is clear of developer errors or more so know as syntax errors so that the queries can be utilized as intended. Each individual query text or command has its uses, for example we can use .find(), .findOne(), etc, to find documents withing a database, .update() is utuilized with generally two enrtries as the new entry is provided as well as the old entry that will eventually be replaced. The .delete() function or .deleteMany() comands are used to delete quries one or many documents. The .create() likewise as the name suggests, creates new document entried to the collectiona and database. Utilizing and understanding these commands can help implement any kind of user interface as long as the language or framework in question supports MongoDB. MongoDB however, is not the only database as there are a wide variety of database software that allow the end user and developers to use CRUD and further edit databases. Wether we like to or not 
How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?
What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?


