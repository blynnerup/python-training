def contains_purple(*args):
    return True if "purple" in args else False

print(contains_purple(25, "purple"))
print(contains_purple("green", False, 37, "blue", "hello world"))

# Unpacking of args
# Unpacks a collection and passes individual components
def sum_all_values(*args):
    print(args)
    total = 0
    for num in args:
        total += num
    print(total)

nums = (1,2,3,4,5,6)
sum_all_values(*nums)