def product(int1, int2):
    """Multiply two numbers"""
    return int1 * int2

print (product(2,4))

def return_day(day_int):
    days_to_int = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday"}
    if day_int < 1 or day_int > 7:
        return None
    else:
        return days_to_int.get(day_int)
    
print(return_day(0))
print(return_day(6))

def last_element(elements):
    try:
        return elements.pop()
    except IndexError as e:
        return None
    
print(last_element(["dongle", "bongle"]))
print(last_element([]))


def number_compare(int1, int2):
    if int1 > int2:
        return "First is greater"
    elif int1 < int2:
        return "Second is greater"
    return "Numbers are equal"

print(number_compare(2,1))
print(number_compare(1,2))
print(number_compare(2,2))

def single_letter_count(word, letter):
    return word.lower().count(letter.lower())

print(single_letter_count("hello", "l"))
print(single_letter_count("Hello", "h"))
print(single_letter_count("hello", "w"))

def multiple_letter_count(word):
    return {letter: word.count(letter) for letter in word}

print(multiple_letter_count("hello"))   

def list_manipulation(ls, command, location, value = None):
    if (command == "remove" and location == "end"):
        return ls.pop()
    elif (command == "remove" and location == "beginning"):
        return ls.pop(0)
    elif (command == "add" and location == "end"):
        ls.append(value)
        return ls
    elif (command == "add" and location == "beginning"):
        ls.insert(0, value)
        return ls
    
 
print(list_manipulation([1,2,3], "remove", "end", 4))
print(list_manipulation([1,2,3], "add", "end", 4))
print(list_manipulation([1,2,3], "add", "beginning", 4))

def is_palindrome(string):
    stripped = string.replace(" ", "").lower()
    return stripped == stripped[::-1]

print(is_palindrome("a man a plan a canal Panama"))

def frequency(ls, search):
    return ls.count(search)

print(frequency([1,2,3,4,4], 4))

def multiply_even_numbers(ls):
    sum = 1
    for int in ls:
        if int % 2 == 0:
            sum = sum * int
    return sum

print(multiply_even_numbers([2,3,4]))

def capitalize(string):
    """Slice the first letter , upper case it and then add it to the rest"""
    return string[:1].upper() + string[1:]

print(capitalize("jamaica"))

def compact(ls):
    return [val for val in ls if val]

print(compact([0,1,2,"",[], False, {}, None, "All done"]))

def intersection(ls1, ls2):
    return [el for el in ls1 if el in ls2]

print(intersection([1,2,3], [2,3,4]))
print(intersection(['a','b','z'], ['x','y','z']))

def isEven(num):
    return num % 2 == 0

def partition(ls, fn="isEven"):
    truthy_list = []
    falsy_list = []
    for el in ls:
        if fn(el):
            truthy_list.append(el)
        else:
            falsy_list.append(el)
    return [truthy_list, falsy_list]

# alternavtive
# return [[val for val in lst if fn(val)], [val for val in lst if not
# alternative 2
# return [[l.pop(l.index(i)) for i in l if callback(i)],l]

print(partition([1,2,3,4], isEven))

def extract_full_name(ls):
    return list(map(lambda val: f"{val['first']} {val['last']}", ls))

names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
print(extract_full_name(names))