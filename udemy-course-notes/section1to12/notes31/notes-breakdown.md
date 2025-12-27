## 🧩 **Snippet’s Intent**

> To teach how to use **functions with return values inside loops** — applying the same calculation (here, VAT addition) to multiple data items.

---

### 🧱 1️⃣ Function Definition

```python
def add_vat(price, vat_rate):
    return price * (100 + vat_rate) / 100
```

This function takes:

* `price` → the base price of an item (like ₹100)
* `vat_rate` → the VAT percentage (e.g., 10 for 10%)

It **returns** the total price *including VAT*.

#### 🧮 Example:

If `price = 100` and `vat_rate = 10`,

```
= 100 * (100 + 10) / 100
= 100 * 110 / 100
= 110
```

✅ Returned value → `110`

---

### 🧾 2️⃣ The List of Orders

```python
orders = [100, 150, 200]
```

This represents multiple base prices — maybe for different orders.

---

### 🔁 3️⃣ Looping Through Orders

```python
for price in orders:
    final_amount = add_vat(price, 10)
    print(f"Original: {price}, Final with VAT: {final_amount}")
```

* The loop goes through each `price` in the list.
* For each one:

  * Calls `add_vat()` with a `vat_rate` of 10%.
  * Stores the result in `final_amount`.
  * Prints both original and VAT-included price.

✅ **Output:**

```
Original: 100, Final with VAT: 110.0
Original: 150, Final with VAT: 165.0
Original: 200, Final with VAT: 220.0
```

---

### 🧠 4️⃣ Key Concepts Illustrated

| Concept                      | Explanation                                                |
| ---------------------------- | ---------------------------------------------------------- |
| **Function return values**   | `add_vat()` computes and returns a result for each call    |
| **Loop integration**         | Functions can be called inside loops for repeated use      |
| **Mathematical expressions** | Arithmetic inside the return statement                     |
| **f-strings**                | For clean formatted printing                               |
| **Reusability**              | Same function can be applied to any price list or VAT rate |

---

### ⚙️ 5️⃣ Analogy

Think of it like a **cash register system**:

* You have a list of items (`orders`)
* Each item goes through a **VAT calculator** (`add_vat`)
* The system prints both original and final totals

---

### 💡 Bonus Tip

If you wanted to collect all final prices in a list:

```python
final_amounts = [add_vat(price, 10) for price in orders]
print(final_amounts)
```

Output:

```
[110.0, 165.0, 220.0]
```

That’s a **list comprehension** version — compact and Pythonic.

---

So this file connects three big Python ideas:

> ✅ *Functions that return values*
> ➕ *Loops that apply them repeatedly*
> ➕ *Lists that store and iterate over multiple data items*