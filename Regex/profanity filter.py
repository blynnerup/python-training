import re

def censor(user_input):
    profanity_pattern = re.compile(r'(frack[a-z]*)', re.IGNORECASE)
    altered_text = profanity_pattern.sub("CENSORED", user_input)
    return altered_text

print(censor("Frack you"))
print(censor("I hope you fracking die"))
print(censor("you fracking Frack"))