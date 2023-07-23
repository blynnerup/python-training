firstList = [1,2,3,4]
secondList = [3,4,5,6]

answer = [num for num in firstList if num in secondList]
print(answer)

nameList = ["Ellie", "Tim", "Matt"]
reversed = [name[::-1].lower() for name in nameList]

print(reversed)

twelveList = [num for num in range(1, 101) if num % 12 == 0]
print(twelveList)

noVowels = [char for char in "amazing" if char not in "aeiou"]
print(noVowels)

# Nested List
nested = [[num for num in range(0,3)] for count in range(1,4)]
print(nested)

giantNest = [[num for num in range(0,10)] for count in range(1,11)]
print(giantNest)

