print("----------------------")
print("Start valid_parentheses")
"""
Write a function called valid_parentheses that takes a string of parentheses,
and determines if the order of the parentheses is valid.
valid_parentheses should return true if the string is valid, and false if it's invalid.
"""

def valid_parentheses(object):
    while len(object) != len(object.replace("()","")):
        object = object.replace("()","")
    return object == ""

print(valid_parentheses("()"))
print(valid_parentheses(")(()))"))
print(valid_parentheses("("))
print(valid_parentheses("(())((()())())"))
print(valid_parentheses('))(('))
print(valid_parentheses('())('))
print(valid_parentheses('()()()()())()('))

print("End valid_parentheses")
print("----------------------")
print("Start reverse_vowels")
"""
Write a function called reverse_vowels.
This function should reverse the vowels in a string.
Any characters which are not vowels should remain in their original position.
You should not consider "y" to be a vowel.
"""

def reverse_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', "I", "O", "U"]
 
    vowel_idx = [ str.index(char) for char in str if char in vowels]
    reverse_idx = list(reversed(vowel_idx))
       
    i = 0
    new_str = ""
    for c in str:
      if c not in vowels:
        new_str += c
      else:
        new_str += str[reverse_idx[i]]
        i += 1
    return new_str

print(reverse_vowels("Hello!"))
print(reverse_vowels("Tomatoes"))
print(reverse_vowels("Reverse Vowels In A String"))

print("End reverse_vowels")
print("----------------------")
print("Start three_odd_numbers")