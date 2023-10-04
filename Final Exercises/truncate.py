"""
Write a function called truncate that will shorten a string to a specified length,
and add "..." to the end.  Given a string and a number n,
truncate the string to a shorter string containing at most n characters. 
"""
def truncate(input_str, truncation_length):
    if(truncation_length < 3):
        return "Truncation must be at least 3 characters."
    elif (truncation_length > len(input_str)):
        return input_str
    return input_str[:truncation_length - 3] + "..."
    

print(truncate("Super cool", 2))
print(truncate("Super cool", 1))
print(truncate("Holy guacamole!", 152))
print(truncate("Yo",100))
print(truncate("Hello World", 6))
print(truncate("Problem solving is the best!", 10))
print(truncate("Woah", 4))
print(truncate("Woah", 3))