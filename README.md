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

Writing programs that are maintainable, readable, and adaptable is crucial for efficient software development. In the context of the CRUD Python module used in Project One and Project Two, there are several advantages to working in this manner.

To achieve maintainability, it is important to structure the code in a modular and organized way. This includes breaking down the functionality into smaller, reusable functions or classes. By encapsulating specific operations within functions or classes, it becomes easier to understand and maintain the code. Additionally, using meaningful variable and function names, as well as adding comments where necessary, improves code readability and makes it easier for others (including future you) to comprehend the codebase.

Adaptability is achieved by writing flexible code that can handle changes and updates smoothly. In the case of the CRUD Python module, it should be designed to handle different database configurations and adapt to future modifications. This can be achieved by using configuration files or parameters that allow easy modification of database connection details, such as username, password, host, and port. By decoupling the database-specific code from the rest of the application, it becomes easier to switch databases or make changes to the underlying database system without affecting the overall functionality.

The advantages of working with a CRUD Python module are numerous. It promotes code reusability, as the module can be used across multiple projects or modules within the same project. It also enhances maintainability, as any changes or updates to the database operations can be done in a single place (the module) rather than scattered throughout the codebase. This simplifies debugging and reduces the chances of introducing errors. Furthermore, using a module like this improves code readability and allows developers to focus on the core business logic of their applications rather than low-level database operations.

In the future, this CRUD Python module can be extended and utilized in various ways. For instance, it can be integrated with other frameworks or libraries to develop web applications, API endpoints, or data processing pipelines. By leveraging the module's functionality, developers can easily perform CRUD operations on different database systems, such as MySQL, PostgreSQL, or SQLite. This reusability and adaptability save time and effort in future development projects.

As a computer scientist, the approach to problem-solving involves breaking down complex problems into smaller, manageable components. When tackling the database or dashboard requirements of Grazioso Salvare, a similar approach would be taken. The project would start with understanding the client's needs and requirements, identifying the necessary data structures, and designing a suitable database schema. The CRUD Python module would be utilized to implement the required functionality, ensuring the code is maintainable, readable, and adaptable.

In comparison to previous assignments in other courses, the project for Grazioso Salvare may differ in terms of scope, complexity, or specific technologies used. However, the fundamental problem-solving approach remains the same: understanding requirements, designing appropriate solutions, and implementing them effectively.

To create databases to meet other client requests in the future, several techniques and strategies can be employed. This includes conducting thorough requirement analysis, properly designing the database schema, and using normalization techniques to ensure data integrity and reduce redundancy. It is important to consider the anticipated scale and performance requirements of the database and select suitable technologies accordingly. Regular testing, performance optimization, and security considerations should also be part of the development process.

Computer scientists work on a variety of tasks, including designing algorithms, developing software, analyzing and interpreting data, and solving complex problems. Their work is essential as it contributes to advancements in technology, enables automation, improves efficiency, and facilitates decision-making processes. Computer scientists help create innovative solutions, develop robust systems, and provide insights into various domains, impacting industries, businesses, and society as a whole.


