## 🧩 **Snippet’s Intent:**

> To introduce **dictionaries (dict)** in Python — a data type that stores **key-value pairs** and allows fast lookups, updates, and deletions.

---

## 🔹 1️⃣ Creating a dictionary directly

```python
chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"Chai order: {chai_order}")
```

✅ **Explanation:**

* `dict()` is used to create a dictionary.
* Keys: `"type"`, `"size"`, `"sugar"`
* Values: `"Masala Chai"`, `"Large"`, `2`

✅ **Output:**

```
Chai order: {'type': 'Masala Chai', 'size': 'Large', 'sugar': 2}
```

---

## 🔹 2️⃣ Creating and modifying a dictionary dynamically

```python
chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"
```

✅ **Explanation:**

* Start with an **empty dict** `{}`.
* Add new **key-value pairs** dynamically using assignment syntax:

  * `"base": "black tea"`
  * `"liquid": "milk"`

✅ **Output:**

```
Recipe base: black tea
Recipe: {'base': 'black tea', 'liquid': 'milk'}
```

---

## 🔹 3️⃣ Deleting a key-value pair

```python
del chai_recipe["liquid"]
print(f"Recipe: {chai_recipe}")
```

✅ **Explanation:**

* `del dict[key]` removes the entry for that key.

✅ **Output:**

```
Recipe: {'base': 'black tea'}
```

---

## 🔹 4️⃣ Membership testing

```python
print(f"Is sugar in the order? {'sugar' in chai_order}")
```

✅ **Explanation:**

* `'key' in dict` checks if a key exists.

✅ **Output:**

```
Is sugar in the order? True
```

---

## 🔹 5️⃣ Accessing dictionary details

```python
chai_order = {"type": "Ginger Chai", "size": "Medium", "sugar": 1}
# print(f"Order details (keys): {chai_order.keys()}")
# print(f"Order details (values): {chai_order.values()}")
# print(f"Order details (items): {chai_order.items()}")
```

✅ **Explanation:**

* `.keys()` → returns all keys
* `.values()` → returns all values
* `.items()` → returns key-value pairs (as tuples)

---

## 🔹 6️⃣ Removing the last item

```python
last_item = chai_order.popitem()
print(f"Removed last item: {last_item}")
```

✅ **Explanation:**

* `.popitem()` removes and returns the **last inserted** key-value pair (as a tuple).

✅ **Example Output:**

```
Removed last item: ('sugar', 1)
```

→ **LIFO-style removal** from dictionaries (Python 3.7+ preserves insertion order).

---

## 🔹 7️⃣ Updating with another dictionary

```python
extra_spices = {"cardamom": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)
print(f"Updated chai recipe: {chai_recipe}")
```

✅ **Explanation:**

* `.update()` merges another dictionary into the existing one.
* Adds new key-value pairs or updates existing ones.

✅ **Output:**

```
Updated chai recipe: {'base': 'black tea', 'cardamom': 'crushed', 'ginger': 'sliced'}
```

---

## 🔹 8️⃣ Safe value retrieval with `.get()`

```python
customer_note = chai_order.get("size", "NO Note")
print(f"customer_note is: {customer_note}")
```

✅ **Explanation:**

* `.get(key, default)` returns the value if key exists, else returns the default value (avoids `KeyError`).

✅ **Output:**

```
customer_note is: Medium
```

---

## ✅ Summary Table

| Operation         | Example                                 | Description                      |
| ----------------- | --------------------------------------- | -------------------------------- |
| Create dict       | `d = dict(a=1, b=2)`                    | Create using `dict()`            |
| Add key-value     | `d["x"] = 10`                           | Insert new item                  |
| Delete key        | `del d["x"]`                            | Remove a specific key            |
| Membership test   | `'x' in d`                              | Check if key exists              |
| Keys/Values/Items | `d.keys()` / `d.values()` / `d.items()` | Inspect structure                |
| Remove last       | `d.popitem()`                           | Remove and return last key-value |
| Merge             | `d.update(d2)`                          | Combine two dictionaries         |
| Safe access       | `d.get("key", default)`                 | Avoid errors for missing keys    |

---

## 🧠 Key Takeaways

* A **dictionary** maps **unique keys → values**.
* It’s **unordered (until Python 3.6)** but preserves **insertion order** now.
* Supports fast lookups and updates (via hashing).
* Ideal for representing structured or labeled data (like JSON).