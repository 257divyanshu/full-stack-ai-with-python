## 🧩 **Snippet’s Intent:**

> To teach how to write **compact conditional expressions** (also called **ternary operators**) in Python — a shorthand for simple `if/else` logic.

---

## 🔹 1️⃣ Taking input and converting type

```python
order_amount = int(input("Enter the order amount: "))
```

✅ **Explanation:**

* `input()` always returns a **string**, even if you type a number.
* Wrapping it in `int()` converts it into an **integer**, so we can perform numeric comparisons (`> 300`).

✅ Example:

```
Enter the order amount: 450
```

→ `order_amount = 450` (as an integer)

---

## 🔹 2️⃣ Conditional (Ternary) Expression

```python
delivery_fees = 0 if order_amount > 300 else 30
```

✅ **Explanation:**
This is a **one-line version** of:

```python
if order_amount > 300:
    delivery_fees = 0
else:
    delivery_fees = 30
```

So:

* If `order_amount > 300`, delivery fee = 0
* Otherwise, delivery fee = 30

✅ Example:

| Input | Output                  |
| ----- | ----------------------- |
| `450` | `Delivery fees is : 0`  |
| `250` | `Delivery fees is : 30` |

🧩 **Concept taught:**
→ How to **assign values conditionally** in a single expression — great for simple decisions.

---

## 🔹 3️⃣ Output

```python
print(f"Delivery fees is : {delivery_fees}")
```

✅ Uses an **f-string** for formatted output.

---

## ✅ Summary Table

| Concept           | Code                           | Explanation                        |
| ----------------- | ------------------------------ | ---------------------------------- |
| Get numeric input | `int(input())`                 | Convert user input to integer      |
| Ternary operator  | `x if cond else y`             | One-line conditional assignment    |
| Example           | `fee = 0 if amt > 300 else 30` | Assign 0 or 30 depending on amount |

---

## 🧠 Key Takeaways

* The **ternary expression** is ideal for short, simple conditions.
* Always **convert user input** to the right type (`int`, `float`, etc.).