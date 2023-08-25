# To run a doctest in a python file run the following line (make sure terminal is in same folder as file)
# python3 -m doctest -v <filename>

def add(num1, num2):
    """
    Returns the added value of num1 and num2
    >>> add(1,3) 
    4
    >>> add(4,8) 
    12
    """
    return num1 + num2

def sub(num1, num2):
    """ Returns the subtracted value of num2 from num1

    >>> sub(3,1)
    2

    >>> sub(4,5)
    -1

    """
    return num1 - num2