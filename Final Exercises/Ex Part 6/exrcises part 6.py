print("----------------------")
print("Start letter_counter")
"""
Write a function called letter_counter which accepts a string and returns a function.
When the inner function is invoked it should accept a parameter which is a letter,
and the inner function should return the number of times that letter appears.
This inner function should be case insensitive.
"""

def letter_counter(input_str):
    def inner(letter):
        lower_str = input_str.lower()
        return lower_str.count(letter)
    return inner

counter = letter_counter('Amazing')
print(counter('a'))
print(counter('m'))

counter2 = letter_counter('This Is Really Fun!')
print(counter2('i'))
print(counter2('t'))

print("End letter_counter")
print("----------------------")
print("Start once")
"""
Write a function called once.
This function accepts a function and returns a new function that can only be invoked once.
If the function is invoked more than once,
it should return None.
Hint you will need to define a new function inside of your once function and return that function.
You can add properties to your inner function to see if it has run already.
"""

def add(a, b):
    return a + b

def once(func):
    func.called_once = False
    def inner(*args):
        if not func.called_once:
            func.called_once = True
            return func(*args)
    return inner

oneAddition = once(add)
print(oneAddition(2,2))
print(oneAddition(2,2))
print(oneAddition(12,200))

print("End once")
print("----------------------")
print("Start next_prime")
"""
Write a function called next_prime,
which returns a generator that will yield an unlimited number of primes starting from the first prime (2).
Recall that a prime number is any whole number that has exactly two divisors: one and the number itself.
The first few primes are 2, 3, 5, 7, 11, ...
"""

def next_prime():
    num = 2
    all_primes = set()
    while True:
        for prime in all_primes:
            if num % prime == 0:
                break
        else:
            all_primes.add(num)
            yield num
        num += num % 2 + 1


d = next_prime()
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
