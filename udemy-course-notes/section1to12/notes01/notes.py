# 📍 id() function
# - see id-function.md
# ☑️ example (id varies each run)
# role = "full-stack developer"
# print(id(role)) 
# ☑️ example (Same object, same id)
# a = 5
# b = a
# print(id(a))
# print(id(b))
# - Both a and b have the same id → they point to the same object in memory.
# ☑️ example (Different object, different id)
# a = [1, 2, 3]
# b = [1, 2, 3]
# print(id(a))
# print(id(b))
# - Even though the lists look the same, they’re two separate objects in memory.
# ☑️ example (Changing variable vs changing object)
# x = 10
# print(id(x))  # e.g. 100
# x = 20
# print(id(x))  # e.g. 120
# - Notice how x now points to a different object — integers are immutable, so Python doesn’t change the existing one; it creates a new one.
# ☑️ example (Mutable object)
# nums = [1, 2, 3]
# print(id(nums))
# nums.append(4)
# print(id(nums))
# - Same ID — because lists are mutable, Python modifies the object in place.

# 📍 f strings
# role = 'full-stack developer'
# intro = f'I am a {role}'
# print(intro)