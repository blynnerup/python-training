from functools import wraps

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