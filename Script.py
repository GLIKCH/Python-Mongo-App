# Joel De Alba
# Southern New Hampshire University
# 06/30/23
# Professor Dr. Tad Kellog

# Sys import for closing app
import sys

# Importing the Animal Shelter Python Script
from AnimalShelter import AnimalShelter

# pulling data from AnimalShelter.py
a = AnimalShelter()
r = AnimalShelter.read()
c = AnimalShelter.create()
u = AnimalShelter.update()
d = AnimalShelter.delete()

# Function that initiates functionality information
def initInfo():
    print("Welcome to Global Rain CRUD Management Application\n"
          "This application will sample an AnimalShelter database to educate\n"
          "on CRUD methodologies for Python and MongoDB database functions\n"
          "Select an option.\n"
          "[1] Read Collection(s)\n"
          "[2] Create Collection(s)\n"
          "[3] Update Collection(s)\n"
          "[4] Delete Collection(s)\n"
          "\n\n If you would like to close the application press any key")
    i = input("\n--| ")
    if i == '1':
        return r
    elif i == '2':
        return c
    elif i == '3':
        return u
    elif i == '4':
        return d
    else:
        print("Invalid option selected.")
        sys.exit("")


# Call the function
initInfo()
