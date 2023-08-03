list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

answer = {list1[i]: list2[i] for i in range(0, len(list1))}
print(answer)

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
# personDict = [item for item in person]
personDict = {item[0]: item[1] for item in person}
print(personDict)

# Alternate version
personDict2 ={k: v for k,v in person}
print(personDict2)

ascii_list = {num: chr(num) for num in range(65, 91)}
print(ascii_list)
