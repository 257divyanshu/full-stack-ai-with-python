class Chaicup:
    size = 150 #ml

    def describe(self):
        return f"A {self.size}ml chai cup"
    

cup = Chaicup()
print(cup.describe()) # A 150ml chai cup
print(Chaicup.describe(cup)) # A 150ml chai cup
# print(Chaicup.describe()) # TypeError: Chaicup.describe() missing 1 required positional argument: 'self'

cup_two = Chaicup()
cup_two.size = 100
print(Chaicup.describe(cup_two)) # A 100ml chai cup