print("----------------------")
print("Start sum_up_diagonals")

"""
Write a function called sum_up_diagonals which accepts an NxN list of lists
and sums the two main diagonals in the array:
the one from the upper left to the lower right, and the one from the upper right to the lower left.
"""
def sum_up_diagonals(matrix_list):
    rows = len(matrix_list)
    sum = 0
    # Diagonal from top left
    for i in range(0, rows):
        sum += matrix_list[i][i]
    # Diagonal from bottom left
    for j in range(0, rows):
        sum += matrix_list[rows - j - 1][j]
    print(sum)
    return sum

list1 = [
  [ 1, 2 ],
  [ 3, 4 ]
]
sum_up_diagonals(list1)

list2 = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]
sum_up_diagonals(list2)

list3 = [
  [ 4, 1, 0 ],
  [ -1, -1, 0],
  [ 0, 0, 9]
]
sum_up_diagonals(list3)

print("End sum_up_diagonals")
print("----------------------")
print("Start min_max_key_in_dictionary")

"""
Write a function called min_max_key_in_dictionary which returns a list
with the lowest key in the dictionary and the highest key in the dictionary.
You can assume that the dictionary will have keys that are numbers.
"""
def min_max_key_in_dictionary(input_dict):
    dict_keys = input_dict.keys()
    return [min(dict_keys), max(dict_keys)]

print(min_max_key_in_dictionary({2:'a', 7:'b', 1:'c',10:'d',4:'e'}))
print(min_max_key_in_dictionary({1: "Elie", 4:"Matt", 2: "Tim"}))

print("End min_max_key_in_dictionary")
print("----------------------")
print("Start find_greater_numbers")

"""
Write a function called find_greater_numbers which accepts a list
and returns the number of times a number is followed by a larger number across the entire list. 
"""
def find_greater_numbers(input_list):
    return sum(x < y for i,x in enumerate(input_list) for y in input_list[i:])

print(find_greater_numbers([1,2,3]))
print(find_greater_numbers([6,1,2,7]))
print(find_greater_numbers([5,4,3,2,1]))
print(find_greater_numbers([]))

print("End find_greater_numbers")
print("----------------------")
print("Start two_oldest_ages")

"""
Write a function called two_oldest_ages.
The function should take a list of numbers as its argument
and return the two highest numbers within the list.
The returned value should be a list in the format [second oldest age, oldest age].

The order of the numbers passed in could be any order.
"""
def two_oldest_ages(ages):
    return sorted(ages)[-2:]

print(two_oldest_ages( [1, 2, 10, 8] ))
print(two_oldest_ages( [6,1,9,10,4] ))
print(two_oldest_ages( [4,25,3,20,19,5] ))

print("End two_oldest_ages")
print("----------------------")
print("Start is_odd_string")

"""
Write a function called is_odd_string which returns true
if sum of each character's position in the alphabet is odd.
For example, "a" is in the first position, "b" is in the second position, and so on.
If the sum is even, return false. 
NOTE: INDEXING STARTS AT 1.  A is position 1, NOT POSITION 0.
"""

def is_odd_string(str):
#generating a list of all alphabets by using chr() and ord() inbuilt methods.
		alphabets_list = list(map(chr, range(ord('a'), ord('z')+1)))
		sum=0
		for alpha in str:
			sum+=(alphabets_list.index(alpha)+1)
		if sum%2==0:
			return False
		else:
			return True

print(is_odd_string('a'))
print(is_odd_string('aaaa'))
print(is_odd_string('amazing'))
print(is_odd_string('veryfun'))
print(is_odd_string('veryfunny'))