# 📍 sets
# - see sets-guide.md
# ☑️ example (type of set)
# set1 = set() 
# print(type(set1)) # <class 'set'>
# ☑️ example (creting an empty set)
# empty1 = set()   # ✅ Correct
# empty2 = {}      # ❌ Creates an empty dict, not a set
# print(type(empty1)) # <class 'set'>
# print(type(empty2)) # <class 'dict'>
# - sets are unindexed
# - sets are mutable
# - elements inside sets must be immutabe (numbers, strings, tuples)
# - discard() is safer than remove()
# - pop() removes an element randomly
# - sets offer fast membership checking
# - frozneset is set's immutable cousin
# ☑️ example (for mutable objects, id doesn't change on modifying)
# set1 = set([1,2,3])
# print(id(set1))
# set1.add(4)
# print(id(set1)) # the id remains same