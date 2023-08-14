import father
import mother

class Child(mother, father):
    pass

c = Child()
print(help(c))