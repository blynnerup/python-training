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