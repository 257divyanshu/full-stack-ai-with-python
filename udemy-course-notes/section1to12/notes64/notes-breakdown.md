## ☕ Code Recap

```python
def process_order(item, quantity):
    try:
        price = {"masala": 20}[item]
        cost = price * quantity
        print(f"total cost is {cost}")
    except KeyError:
        print("Sorry that chai is not on menu")
    except TypeError:
        print("Quantity must be a number")

process_order("ginger", 2)
process_order("masala", "two")
```

---

## 🧩 Step-by-step Explanation

### 1. **`try` block**

```python
price = {"masala": 20}[item]
cost = price * quantity
```

* Attempts to:

  1. Look up the price in the dictionary.
  2. Multiply price by quantity.

* Both actions **might fail**, triggering exceptions.

---

### 2. **Multiple `except` blocks**

```python
except KeyError:
    print("Sorry that chai is not on menu")
except TypeError:
    print("Quantity must be a number")
```

* **`KeyError`** → occurs when `item` is not in the dictionary (`"ginger"` is missing).
* **`TypeError`** → occurs when you try to multiply a number by a string (`20 * "two"`).

Python executes **the first matching except block** for the raised exception.

---

### 3. **Program flow**

#### Case 1: `"ginger", 2`

* `"ginger"` is **not in the dictionary**, raises `KeyError`.
  Output:

```
Sorry that chai is not on menu
```

#### Case 2: `"masala", "two"`

* `"masala"` exists → price = 20
* Multiplying `20 * "two"` → raises `TypeError`
  Output:

```
Quantity must be a number
```

---

### ✅ Key Takeaways

| Concept           | Explanation                                       |
| ----------------- | ------------------------------------------------- |
| Multiple `except` | Handle different exceptions separately            |
| `KeyError`        | Raised when a dictionary key doesn’t exist        |
| `TypeError`       | Raised when an operation receives an invalid type |
| Flow              | Only the first matching `except` runs             |

---

💡 **Tip:** You can also handle **all exceptions together** using:

```python
except (KeyError, TypeError) as e:
    print("Error:", e)
```