favourite_chais = [
    "Masala Chai", "Green Tea", "Masala Chai",
    "Lemon Tea", "Green Tea", "Elaichi Chai"
]

unique_chai = {chai for chai in favourite_chais}
print(unique_chai)


recipes = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elaichi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"],
}

# unique_spices = {ingredients for ingredients in recipes.values()} # TypeError: cannot use 'list' as a set element (unhashable type: 'list')

# unique_spices = {ingredient for ingredient in ingredients for ingredients in recipes.values()} # NameError: name 'ingredients' is not defined

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

# ❔1️⃣ breakdown the above set comprehension

print(unique_spices)