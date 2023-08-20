def get_multiples(num = 1, count = 10):
    for value in range(1, count + 1):
        yield num * value

d = get_multiples(2, 3)
print(next(d))
print(next(d))
print(next(d))
