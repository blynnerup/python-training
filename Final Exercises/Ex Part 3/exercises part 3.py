# In order to keep file count lower, the exercises will be bundled together.
print("Start two_list_dictionary")
def two_list_dictionary(list_of_keys, list_of_values):
    key_values_dict = {}
    for idx, val in enumerate(list_of_keys):
        if idx < len(list_of_values):
            key_values_dict[list_of_keys[idx]] = list_of_values[idx]
        else:
            key_values_dict[list_of_keys[idx]] = None
    return key_values_dict

print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]))
print(two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4]))
print(two_list_dictionary(['x', 'y', 'z']  , [1,2]))

print("End two_list_dictionary")
print("----------------------")
print("Start range_in_list")

def range_in_list(lst, start=0, end=None):
    end = end or lst[-1]
    return sum(lst[start:end+1])

print(range_in_list([1,2,3,4],0,2))
print(range_in_list([1,2,3,4],0,3))
print(range_in_list([1,2,3,4],1))
print(range_in_list([1,2,3,4]))

print("End range_in_list")
print("----------------------")
print("Start same_frequency")

"""
Write a function called same_frequency which accepts two numbers
and returns True if they contain the same frequency of digits. Otherwise, it returns False.
"""

def same_frequency(num_1, num_2):
    num_1_as_str = str(num_1)
    num_2_as_str = str(num_2)

    if len(num_1_as_str) != len(num_2_as_str):
        return False
    
    for i in range(len(num_1_as_str)):
        if num_1_as_str[i] in num_2_as_str:
            num_2_as_str = num_2_as_str.replace(num_1_as_str[i], '', 1)
        else:
            return False
    return True

print(same_frequency(551122,221515))
print(same_frequency(321142,3212215))
print(same_frequency(1212, 2211))
print(same_frequency(1213, 2211))

print("End same_frequency")
print("----------------------")
print("Start nth")

"""
Write a function called nth,
which accepts a list and a number and returns the element at whatever index is the number in the list.
If the number is negative, the nth element from the end is returned.

You can assume that number will always be between the negative value of the list length,
and the list length minus 1.
"""

def nth(list_of_elements, index):
    el_at_nth = None
    if index >= 0:
        el_at_nth = list_of_elements[index]
    else:
        el_at_nth = list_of_elements[index + len(list_of_elements)]
    return el_at_nth

print(nth(['a', 'b', 'c', 'd'], 1))
print(nth(['a', 'b', 'c', 'd'], -2))
print(nth(['a', 'b', 'c', 'd'], 0))
print(nth(['a', 'b', 'c', 'd'], -4))

print("End nth")
print("----------------------")
print("Start find_the_duplicate")

def find_the_duplicate(arr):
    counter = {}
    for val in arr:
        if val in counter:
            counter[val] += 1
        else:
            counter[val] = 1
    for key in counter.keys():
        if counter[key] > 1:
            return int(key)

    