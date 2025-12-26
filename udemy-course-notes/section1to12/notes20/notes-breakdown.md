## 🧩 **Snippet’s Intent**

> To teach how to **iterate over a list with access to both the element and its index** using `enumerate()`.

---

## 🔹 1️⃣ The `for` loop with `enumerate`

```python
menu = ["Green", "Lemon", "Spiced", "Mint"]

for idx, item in enumerate(menu, start=1):
    print(f"{idx} : {item} chai")
```

✅ **Explanation:**

* `menu` is a list of chai flavors.
* `enumerate(menu, start=1)` returns **pairs of (index, item)**.

  * `start=1` makes counting start from **1** instead of default **0**.
* `idx` → the current index
* `item` → the current element (flavor)

---

## 🔹 2️⃣ Example Output

```
1 : Green chai
2 : Lemon chai
3 : Spiced chai
4 : Mint chai
```

---

## 🔹 3️⃣ Concepts Taught

| Concept           | Explanation                                                      |
| ----------------- | ---------------------------------------------------------------- |
| `enumerate()`     | Returns **(index, element)** pairs while iterating               |
| `start` parameter | Sets the **starting index** (default is 0)                       |
| Loop unpacking    | `for idx, item in ...` unpacks each pair into separate variables |
| f-strings         | Combines index and element into formatted output                 |

---

## 🔹 4️⃣ Tip

* Using `enumerate()` is **cleaner** than:

```python
for i in range(len(menu)):
    print(f"{i+1} : {menu[i]} chai")
```

* Especially useful when you need **both the element and its position**.

---

This builds nicely on your previous list-loop examples, showing a **more advanced, practical iteration technique**.