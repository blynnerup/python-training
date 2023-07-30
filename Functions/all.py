def is_all_strings(iterable):
    return all(isinstance(el, str) for el in iterable)

print(is_all_strings(['a', 'b', 'c']))
print(is_all_strings([2,'a', 'b', 'c']))
print(is_all_strings(('hello', 'goodbye')))