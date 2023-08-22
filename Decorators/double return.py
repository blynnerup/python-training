from functools import wraps
# Exercise 1
def double_return(fn):
    @wraps(fn)
    def double_return_wrapper(*args, **kwargs):
        return [fn(*args, **kwargs), fn(*args, **kwargs)]
    return double_return_wrapper

@double_return 
def add(x, y):
    return x + y
    
add(1, 2)   

@double_return
def greet(name):
    return "Hi, I'm " + name

greet("Colt")

# Exercise 2
def ensure_fewer_than_three_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if len(args) > 2:
            return "Too many arguments!"
        else:
            return fn(*args, **kwargs)
    return wrapper

def add_all(*nums):
    return sum(nums)

add_all(1)
add_all(1,2)

# Exercise 3
def only_ints(fn):
    @wraps(fn)
    def only_ints_wrapper(*args, **kwargs):
        if all(isinstance(x, int) for x in args):
            # print("ok")
            return fn(*args, **kwargs)
        else:
            # print("not ok")
            return("Please only invoke with integers.")
    return only_ints_wrapper

@only_ints 
def add(x, y):
    return x + y
    
add(1, 2)
add("1", "2")
