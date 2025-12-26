## 🧩 **Snippet’s Intent**

> To teach how to **repeat a block of code multiple times** using a `for` loop, and how to generate a sequence of numbers with `range()`.

---

## 🔹 1️⃣ The `for` loop

```python
for token in range(1, 11):
    print(f"Serving chai to Token #{token}")
```

✅ **Explanation:**

* `for token in range(1, 11)` → Loops over numbers **1 through 10** (the stop value `11` is exclusive).
* `token` takes each number in the sequence, one by one.
* The indented block runs **once per number**.

---

## 🔹 2️⃣ Example Output

```
Serving chai to Token #1
Serving chai to Token #2
Serving chai to Token #3
...
Serving chai to Token #10
```

---

## 🔹 3️⃣ Concepts Taught

| Concept              | Explanation                                                     |
| -------------------- | --------------------------------------------------------------- |
| `for` loop           | Repeats a block of code for each item in a sequence             |
| `range(start, stop)` | Generates numbers from `start` up to (but not including) `stop` |
| Loop variable        | `token` holds the current number in each iteration              |
| f-strings            | `f"..."` lets you insert variables into strings easily          |

---

## 🔹 4️⃣ Tip

* You can also use `range(10)` → numbers 0 to 9.
* Combine `range(start, stop, step)` to control the step size:

```python
for token in range(1, 11, 2):  # 1,3,5,7,9
    print(token)
```

---

This example is a **classic beginner-friendly introduction to loops**.