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
