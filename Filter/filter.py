def remove_negatives (ls):
    return list(filter(lambda num: num > -1, ls))

print(remove_negatives([1,3,-5,7,-9, 0]))