def contains_purple(*args):
    return True if "purple" in args else False

print(contains_purple(25, "purple"))
print(contains_purple("green", False, 37, "blue", "hello world"))