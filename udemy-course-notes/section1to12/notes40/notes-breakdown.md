## 🧩 **Snippet’s Intent**

> To show how to quickly build **unique collections** using **set comprehensions**, especially when you want to eliminate duplicates automatically.

---

### 🧠 Code 1 — Remove duplicates

```python
favourite_chais = [
    "Masala Chai", "Green Tea", "Masala Chai",
    "Lemon Tea", "Green Tea", "Elaichi Chai"
]

unique_chai = {chai for chai in favourite_chais }
print(unique_chai)
```

✅ Explanation:

* `{chai for chai in favourite_chais}` → this is a **set comprehension**
* It loops through `favourite_chais`
* Sets **automatically remove duplicates**

🧾 Output example:

```
{'Lemon Tea', 'Green Tea', 'Elaichi Chai', 'Masala Chai'}
```

✅ **Key point:** Order is not guaranteed in sets, but duplicates are gone!

---

### 🧠 Code 2 — Nested set comprehension

```python
recipes = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elaichi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"],
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
print(unique_spices)
```

✅ Step-by-step:

1. `recipes.values()` → gives you lists of ingredients
   (like `["ginger", "cardamom", "clove"]`, etc.)
2. `for ingredients in recipes.values()` → loops through each list
3. `for spice in ingredients` → loops through each spice inside each list
4. `{spice ... }` → collects all unique spices into a **set**

🧾 Output:

```
{'clove', 'milk', 'cardamom', 'black pepper', 'ginger'}
```

---

### 🧠 Key Takeaways

| Concept                  | Explanation                         |
| ------------------------ | ----------------------------------- |
| **Set comprehension**    | Uses `{}` instead of `[]`           |
| **Automatically unique** | Duplicates removed automatically    |
| **Nested loops allowed** | You can have multiple `for` clauses |
| **No guaranteed order**  | Sets are unordered collections      |

---

### 🧪 Example Variations

**Filter Example:**

```python
long_spices = {spice for spice in unique_spices if len(spice) > 5}
```

**Transform Example:**

```python
upper_chais = {chai.upper() for chai in favourite_chais}
```

---