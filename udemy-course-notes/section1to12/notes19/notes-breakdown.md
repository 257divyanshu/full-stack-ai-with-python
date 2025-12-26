## 🧩 **Snippet’s Intent**

> To teach how to **iterate over elements of a list** using a `for` loop.

---

## 🔹 1️⃣ The `for` loop with a list

```python
orders = ["hitesh", "Aman", "Becky", "Carlos"]

for name in orders:
    print(f"Order ready for {name}")
```

✅ **Explanation:**

* `orders` is a **list of customer names**.
* `for name in orders:` → Loops through **each item** in the list.
* `name` takes the value of each list element, one by one.
* The indented block runs **once per element**.

---

## 🔹 2️⃣ Example Output

```
Order ready for hitesh
Order ready for Aman
Order ready for Becky
Order ready for Carlos
```

---

## 🔹 3️⃣ Concepts Taught

| Concept       | Explanation                                                                     |
| ------------- | ------------------------------------------------------------------------------- |
| `for` loop    | Repeats a block of code for each item in a sequence (list, tuple, string, etc.) |
| Loop variable | `name` holds the **current element** during each iteration                      |
| Lists         | `orders = [...]` is a **collection of elements**                                |
| f-strings     | `f"..."` inserts variable values into strings                                   |

---

## 🔹 4️⃣ Tip

* This works for **any iterable**, e.g., lists, tuples, strings, or even dictionaries (keys by default).
* You don’t need indices unless you want them — for just processing items, this is cleaner than using `range(len(list))`.

---

This example complements your previous **`for token in range()`** example, showing that **loops can iterate over numbers or collection elements**.