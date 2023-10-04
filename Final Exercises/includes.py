def includes(collection, value, starting_index = 0):
    if isinstance(collection, dict):
        return value in collection.values()
    else:
        return value in collection[starting_index::]
    
print(includes([1, 2, 3], 1))
print(includes([1, 2, 3], 1, 2))
print(includes('abcd', 'b'))
print(includes('abcd', 'e'))
print(includes({ 'a': 1, 'b': 2 }, 1))
print(includes({ 'a': 1, 'b': 2 }, 'a'))