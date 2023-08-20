def yes_or_no():
    count = 1
    while True:
        count += 1
        if count % 2 == 0:
            yield 'yes'
        else:
            yield 'no'

gen = yes_or_no()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))