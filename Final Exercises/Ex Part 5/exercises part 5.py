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

"""
Write a function called three_odd_numbers,
which accepts a list of numbers and returns True 
if any three consecutive numbers sum to an odd number.
"""

def three_odd_numbers(numbers_list):
   first_three_sum = sum(numbers_list[:2])
   for i in range(2, len(numbers_list)):
      first_three_sum += numbers_list[i]
      if first_three_sum % 2 != 0:
        return True
      first_three_sum -= numbers_list[i - 2]
   else:
      return False

print(three_odd_numbers([1,2,3,4,5]))
print(three_odd_numbers([0,-2,4,1,9,12,4,1,0]))
print(three_odd_numbers([5,2,1]))
print(three_odd_numbers([1,2,3,3,2]))

print("End three_odd_numbers")
print("----------------------")
print("Start mode")

"""
Write a function called mode.
This function accepts a list of numbers and returns the most frequent number in the list of numbers.
You can assume that the mode will be unique.
"""

def mode(numbers_list):
    numbers_dict = {}
    for el in numbers_list:
      if el not in numbers_dict.keys():
         numbers_dict[el] =  1
      else:
         numbers_dict[el] += 1
    return max(numbers_dict, key=numbers_dict.get)

print(mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]))