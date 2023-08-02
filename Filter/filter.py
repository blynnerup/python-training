def remove_negatives (ls):
    return list(filter(lambda num: num > -1, ls))

print(remove_negatives([1,3,-5,7,-9, 0]))

def triple_and_filter(ls):
    return [x * 3 for x in list(filter(lambda x: x % 4 == 0,ls))]

print(triple_and_filter([1,2,3,4]))