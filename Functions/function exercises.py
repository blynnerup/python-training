def product(int1, int2):
    """Multiply two numbers"""
    return int1 * int2

print (product(2,4))

def return_day(day_int):
    days_to_int = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday"}
    if day_int < 1 or day_int > 7:
        return None
    else:
        return days_to_int.get(day_int)
    
print(return_day(0))
print(return_day(6))
