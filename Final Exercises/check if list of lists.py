def list_check(list_check):
    for el in list_check:
        if not isinstance(el, list):
            return False
    return True   

print(list_check([[],[1],[2,3], (1,2)]))
print(list_check([1, True, [],[1],[2,3]]))
print(list_check([[],[1],[2,3]]))
    