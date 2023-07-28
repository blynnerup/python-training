def combine_words(word, **kwargs):
    if len(kwargs) == 0:
        return word
    elif "prefix" in kwargs:
        return kwargs["prefix"] + word
    return word + kwargs["suffix"]
    
print(combine_words("thrall"))
print(combine_words("thrall", prefix="en"))
print(combine_words("thrall", suffix="ed"))

# Unpacking of dictionaries

def display_names(first, second):
    print(f"{first} say hello to {second}")

names = {"first": "Colt", "second": "Rusty"}
display_names(**names)


#Exercise
def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = f"{kwargs.get('message','The result is')} {float(operation_value)}"
    else:
        final = f"{kwargs.get('message','The result is')} {int(operation_value)}"
    return final
    return "The result is " + str(sum)

print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4))
print(calculate(make_float=True, operation='divide', first=3.5, second=5))