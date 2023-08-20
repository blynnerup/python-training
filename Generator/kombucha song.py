def make_song(num_drinks = 99, drink = "soda"):
    while num_drinks > -1:
        if num_drinks == 0:
            yield f"No more {drink}"
        elif num_drinks == 1:
            yield f"Only {num_drinks} bottle of {drink} left!"
        else:
            yield f"{num_drinks} bottles of {drink} on the wall."
        num_drinks -= 1

song = make_song(3, "beer")
print(next(song))
print(next(song))
print(next(song))
print(next(song))
