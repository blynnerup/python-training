"""
Write a function called repeat, which accepts a string and a number and returns a new string
with the string passed to the function repeated the number amount of times. 
Do not use the built in repeat method!
"""

def repeat(input_str, input_num):
    return_str = ""
    while input_num > 0:
        return_str += input_str
        input_num -= 1
    return return_str

print(repeat('*', 3))
print(repeat('abc', 2))
print(repeat('abc', 0))