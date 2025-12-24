### 👉 **Floating-point precision and accuracy in Python**

That’s the core topic.
Everything in this snippet revolves around **how floating-point numbers work** and **why we sometimes need modules like `decimal` or `fractions`** for more precise arithmetic.

---

### 1️⃣ Import statements:

```python
import sys
from fractions import Fraction
from decimal import Decimal
```

These imports give clues about the topic:

* `sys` → used here to inspect floating-point properties (`sys.float_info`)
* `fractions` → for exact rational numbers (e.g., 1/3)
* `decimal` → for high-precision decimal math (e.g., for finance)

---

### 2️⃣ Setting and comparing floating-point numbers:

```python
ideal_temp = 95.5
current_temp = 95.49
```

Both are **floating-point values** (type `float`).

Then:

```python
print(f"Ideal temp { ideal_temp }")
print(f"Current temp { current_temp }")
print(f"Difference temp { ideal_temp - current_temp }")
```

This prints:

```
Ideal temp 95.5
Current temp 95.49
Difference temp 0.009999999999990905
```

💡 Wait — shouldn’t the difference be exactly `0.01`?
That’s the catch!

---

### 3️⃣ The subtle point — **floating-point inaccuracy**

Computers represent floats in **binary**, not decimal.
Some decimal values (like 0.1 or 95.49) **can’t be represented exactly** in binary form, so Python stores a *close approximation*.

That’s why:

```python
95.5 - 95.49  # gives 0.009999999999990905
```

instead of a clean `0.01`.

---

### 4️⃣ Looking at `sys.float_info`

```python
print(sys.float_info)
```

This prints technical details about how Python stores floats, like:

```
sys.float_info(max=1.7976931348623157e+308, 
               max_exp=1024, 
               min=2.2250738585072014e-308, 
               epsilon=2.220446049250313e-16, ...)
```

The key part here is:

```
epsilon=2.220446049250313e-16
```

💡 `epsilon` tells you the *smallest possible difference* Python can distinguish between two float numbers (the precision limit).

---

### 5️⃣ Why `Fraction` and `Decimal` are imported

Though not used yet, they are usually demonstrated right after this code to show **how to fix precision issues**.

For example 👇

#### 🧮 Using `Fraction` for exact ratios:

```python
from fractions import Fraction
print(Fraction(1, 10) + Fraction(2, 10))   # 3/10
```

#### 💵 Using `Decimal` for exact decimal arithmetic:

```python
from decimal import Decimal
a = Decimal("95.5")
b = Decimal("95.49")
print(a - b)  # 0.01  ✅ exact result
```

---

## ✅ Summary:

| Code Section                     | What it shows                              | Concept being taught                    |
| -------------------------------- | ------------------------------------------ | --------------------------------------- |
| `ideal_temp` and `current_temp`  | Float subtraction gives weird result       | Floating-point inaccuracy               |
| `sys.float_info`                 | Technical float details                    | How Python represents floats internally |
| `Fraction` and `Decimal` imports | (used later) exact arithmetic alternatives | How to get rid of float errors          |

---

## 💬 In simple terms:

This snippet taught us:

> “Python’s `float` can’t always represent decimals precisely — here’s proof, here’s why, and here’s how to handle it using `Decimal` or `Fraction`.”