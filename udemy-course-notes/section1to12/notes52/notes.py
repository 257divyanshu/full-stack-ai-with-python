class Chai:
    temperature = "hot"
    strength = "Strong"

cutting = Chai()
print(cutting.temperature) # hot

cutting.temperature = "Mild"
cutting.cup = "small"
print("After changing ",cutting.temperature) # After changing  Mild
print("cup size is  ",cutting.cup) # cup size is   small
print("Direct look into the class ", Chai.temperature) # Direct look into the class  hot

del cutting.temperature
del cutting.cup
print(cutting.temperature) # hot
print(cutting.cup) # AttributeError: 'Chai' object has no attribute 'cup'