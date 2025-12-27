## 🧩 **Snippet’s Intent**

> To teach how to **return a value** from a function and how to **use it in expressions or print statements**.

---

### 🧱 1️⃣ Function Definition

```python
def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup
```

Let’s break it down:

* `def` → defines the function.
* `calculate_bill` → name of the function.
* `(cups, price_per_cup)` → parameters (inputs).
* `return cups * price_per_cup` → sends the result **back** to the caller.

The `return` keyword makes the function **produce an output** — instead of just printing.

---

### 🧮 2️⃣ Function Calls

```python
my_bill = calculate_bill(3, 15)
print(my_bill)
```

Here:

* `cups = 3`
* `price_per_cup = 15`
* The function calculates `3 * 15 = 45`
* That result (`45`) is **returned** and stored in `my_bill`

✅ Output:

```
45
```

---

Next call:

```python
print("Order for table 2: ", calculate_bill(2, 50))
```

* Function calculates `2 * 50 = 100`
* The result (`100`) is returned and printed directly.

✅ Output:

```
Order for table 2:  100
```

---

### 🧠 3️⃣ Key Concepts Illustrated

| Concept                 | Explanation                                                         |
| ----------------------- | ------------------------------------------------------------------- |
| **Return statement**    | Sends a computed value back to where the function was called        |
| **Using return values** | You can store them in variables or use them directly in expressions |
| **Pure functions**      | These functions only compute and return a result — no side effects  |
| **Reusability**         | The same function can calculate any bill with different inputs      |

---

### ⚙️ 4️⃣ Analogy

Think of a function like a **calculator**:

* You give it inputs (`cups`, `price_per_cup`)
* It computes internally
* Then **returns** the final total to you — instead of saying it aloud (printing)

---

### 💡 Bonus Tip

If you **don’t use `return`**, the function implicitly returns `None`.
Example:

```python
def calculate_bill(cups, price_per_cup):
    print(cups * price_per_cup)

print(calculate_bill(3, 15))
```

Output:

```
45
None
```

Because it **prints** the value but doesn’t **return** it.

---

So this example marks your transition from:

> 🗣️ “functions that *say* something”
> to
> 🧮 “functions that *produce* something”