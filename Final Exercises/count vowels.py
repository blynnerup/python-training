def vowel_count(input_str):
    lower_s = input_str.lower()
    return {letter: lower_s.count(letter) for letter in lower_s if letter in "aeiou"}

print(vowel_count('awesome'))
print(vowel_count('Elie'))