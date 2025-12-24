## 🧩 **Snippet’s Intent:**

To demonstrate how **sets** in Python work — how to **combine**, **compare**, and **test membership** efficiently using set operators.

---

## 🔹 1️⃣ Creating Sets

```python
essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}
```

✅ **What this does:**

* Creates two **sets**, which are **unordered** collections of **unique** elements.
* Duplicate values are automatically removed (if any).

🧠 Sets are useful for:

* Mathematical set operations (union, intersection, difference)
* Removing duplicates
* Fast membership checks

---

## 🔹 2️⃣ Union (`|` operator)

```python
all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")
```

✅ **Meaning:**
Union combines all unique elements from both sets.

✅ **Example Output:**

```
All spices: {'cardamom', 'ginger', 'black pepper', 'cloves', 'cinnamon'}
```

---

## 🔹 3️⃣ Intersection (`&` operator)

```python
common_spices = essential_spices & optional_spices
print(f"common spices: {common_spices}")
```

✅ **Meaning:**
Intersection gives you only the **elements common** to both sets.

✅ **Example Output:**

```
common spices: {'ginger'}
```

---

## 🔹 4️⃣ Difference (`-` operator)

```python
only_in_essential = essential_spices - optional_spices
print(f"Only in essential spices: {only_in_essential}")
```

✅ **Meaning:**
Difference gives elements **present in the first set but not in the second**.

✅ **Example Output:**

```
Only in essential spices: {'cardamom', 'cinnamon'}
```

---

## 🔹 5️⃣ Membership Testing (`in` keyword)

```python
print(f"Is 'cloves' in optional spices? {'cloves' in optional_spices}")
```

✅ **Output:**

```
Is 'cloves' in optional spices? True
```

---

## ✅ Summary Table

| Operation        | Syntax     | Meaning            | Example Result              |                        |
| ---------------- | ---------- | ------------------ | --------------------------- | ---------------------- |
| **Intersection** | `A & B`    | Common elements    | `{'b'}`                     |                        |
| **Difference**   | `A - B`    | Elements only in A | `{'a'}`                     |                        |
| **Membership**   | `'x' in A` | Check presence     | `True` / `False`            |                        |

---

## 🧠 Key Takeaways

* **Sets** are unordered and contain **unique** elements.
* They support powerful **mathematical operations** (union, intersection, difference).
* Perfect for **deduplication** and **fast lookups**.