from random import random

def make_noise():
    print("Crowd goes wild!")

make_noise()

def coin_flip():
    # generate a random between 0-1
     r = random()
     if r < 0.5:
          return "Heads"
     else:
          return "Tails"

print(coin_flip())

def generate_evens():
     return [num for num in range(1,50) if num % 2 == 0]

print(generate_evens())

def yell(cry):
     return cry.upper()

print(yell("Upper case this!"))

def exponent(num, power = 2):
     return num ** power

print(exponent(2,3))
print(exponent(3))
print(exponent(power=4, num=4))

def speak(animal = "dog"):
     """This is documentation for a function"""
     if animal == "pig":
          return "oink"
     elif animal == "duck":
          return "quack"
     elif animal == "cat":
          return "meow"
     elif animal == "dog":
          return "woof"
     return "?"

print(speak.__doc__)
print(speak())
print(speak("cat"))
print(speak("whale"))
     