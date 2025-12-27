## 🧩 **Snippet’s Intent**

> To demonstrate how to:
>
> * Store structured data (list of user dictionaries)
> * Use another dictionary as a **lookup table** for coupon-based discounts
> * Use **tuple unpacking** and **default values** with `.get()`
> * Combine both to calculate something dynamically (discounts here)

---

### 🧱 1️⃣ The Data Structures

```python
users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 150, "coupon": "F10"},
    {"id": 3, "total": 80, "coupon": "P50"},
]
```

Each user is a dictionary with:

* `id` → unique identifier
* `total` → total bill amount
* `coupon` → discount code

---

```python
discounts = {
    "P20": (0.2, 0),
    "F10": (0.5, 0),
    "P50": (0, 10),
}
```

This dictionary maps each coupon to a **tuple** of two numbers:

* **first value** → percentage discount
* **second value** → fixed rupee discount

So:

* `"P20"` → 20% off
* `"F10"` → 50% off
* `"P50"` → ₹10 fixed discount

---

### 🧮 2️⃣ The Logic

```python
for user in users:
    percent, fixed = discounts.get(user["coupon"], (0, 0))
    discount = user["total"] * percent + fixed
    print(f"{user['id']} paid {user['total']} and got discount for next visit of rupees {discount}")
```

Let’s unpack what happens here:

#### 🔸 Step 1: Look up discount

`discounts.get(user["coupon"], (0, 0))`

* Looks for the `coupon` key in the `discounts` dictionary.
* Returns `(percent, fixed)` if found, or `(0, 0)` if not (default values).
  → prevents a KeyError if the coupon doesn’t exist.

---

#### 🔸 Step 2: Apply unpacking

`percent, fixed = ...`

This means:

```python
percent = 0.2
fixed = 0
```

(for the first user with coupon `"P20"`)

---

#### 🔸 Step 3: Calculate discount

```python
discount = user["total"] * percent + fixed
```

For each user:

| ID | Total | Coupon | percent | fixed | Discount Formula | Discount Value |
| -- | ----- | ------ | ------- | ----- | ---------------- | -------------- |
| 1  | 100   | P20    | 0.2     | 0     | 100 × 0.2 + 0    | 20             |
| 2  | 150   | F10    | 0.5     | 0     | 150 × 0.5 + 0    | 75             |
| 3  | 80    | P50    | 0       | 10    | 80 × 0 + 10      | 10             |

---

#### 🔸 Step 4: Print formatted string

✅ Output:

```
1 paid 100 and got discount for next visit of rupees 20.0
2 paid 150 and got discount for next visit of rupees 75.0
3 paid 80 and got discount for next visit of rupees 10.0
```

---

### 🧠 Key Concepts Illustrated

| Concept                             | Explanation                                                    |
| ----------------------------------- | -------------------------------------------------------------- |
| **List of dictionaries**            | Represents multiple structured records (like user data)        |
| **Dictionary lookup with `.get()`** | Retrieves a value safely with a default fallback               |
| **Tuple unpacking**                 | Splits returned `(percent, fixed)` into two variables directly |
| **Data-driven logic**               | Instead of hardcoding discounts, it uses reusable mappings     |
| **Formatted f-strings**             | Interpolates variables in user-friendly output                 |

---

### ✨ Real-world Analogy

This is like how an e-commerce site would calculate discounts:

* Each user’s purchase (`users`)
* Uses a centralized discount policy (`discounts`)
* Looks up and applies the right discount automatically

---

### 🧾 Summary of Learning

* Practical use of **nested data structures** (`list` + `dict` + `tuple`)
* Safe lookup with `.get()`
* Smart unpacking and math inside loops
* Data-driven programming (configurable logic, not hardcoded)