# Import the math module:
# Use math.sqrt  to find the square root of 15129 and save it to variable called answer:
import math

answer = math.sqrt(15129)

# Create a function with any number of arguments which returns true or false if a Python keyword is present
import keyword

def contains_keyword(*args):
    return any(-keyword.iskeyword(arg) for arg in args)

print(contains_keyword("hello", "goodbye"))
print(contains_keyword("def", "haha", "lol", "chicken", "alaska"))

import helpers

num = helpers.lucky_number()