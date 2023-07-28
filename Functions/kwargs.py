def combine_words(word, **kwargs):
    if len(kwargs) == 0:
        return word
    elif "prefix" in kwargs:
        return kwargs["prefix"] + word
    return word + kwargs["suffix"]
    
print(combine_words("thrall"))
print(combine_words("thrall", prefix="en"))
print(combine_words("thrall", suffix="ed"))