'''
Ex1:
For this exercise, you'll be working with a file called users.csv.
Each row of data consists of two columns: a user's first name, and a user's last name.

Implement the following function:

add_user : Takes in a first name and a last name and adds a new user to the users.csv file.
add_user("Dwayne", "Johnson") # None
# CSV now has two data rows:

# First Name,Last Name
# Colt,Steele
# Dwayne,Johnson
'''
from csv import writer, DictReader, reader

def add_user(first_name, last_name):
    with open("users.csv", encoding="utf8", mode="a", newline="") as file:
        csv_writer = writer(file)
        csv_writer.writerow([first_name, last_name])

add_user("Dwayne", "Johnson")

'''
Ex2:
Implement the following function:

print_users : prints out all of the first and last names in the users.csv file
print_users() # None
# prints to the console:
# Colt Steele
'''

# def print_users():
#     with open("users.csv", encoding="utf8") as file:
#         csv_reader = DictReader(file)
#         for row in csv_reader:
#             print(row["First Name"] + " " + row["Last Name"])

# print_users()

'''
Ex3:
Implement the following function:

find_user : Takes in a first name and a last name and searches for a user with that first and last name in the users.csv file.
If the user is found, find_user  returns the index where the user is found. 
Otherwise it returns a message stating that the user wasn't found.

find_user("Colt", "Steele") # 1
find_user("Alan", "Turing") # 3
find_user("Not", "Here") # 'Not Here not found.'
'''

def find_user(first_name, last_name):
    with open("users.csv", encoding="utf8") as file:
        csv_reader = reader(file)
        data = list(csv_reader)
        user = [first_name, last_name]
        if user in data:
            return data.index(user)
        return f"{first_name} {last_name} not found."

print(find_user('Colt', 'Steele'))
print(find_user('John', 'Johnson'))