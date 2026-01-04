## ☕ Code Recap

```python
class InvalidChaiError(Exception): pass

def bill(flavor, cups):
    menu = {"masala": 20, "ginger": 40}
    try:
        if flavor not in menu:
            raise InvalidChaiError("that chai is not available")
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be an integer")
        total = menu[flavor] * cups
        print(f"Your bill for {cups} cups of {flavor} chai: rupees {total}")
    except Exception as e:
        print("Error: ", e)
    finally:
        print("Thank you for visiting chaicode!")

bill("mint", 2)
bill("masala", "three")
bill("ginger", 3)
```

---

## 🧩 Step-by-step Explanation

### 1. **Custom Exception**

```python
class InvalidChaiError(Exception): pass
```

* Creates a **specific exception** for invalid chai flavors.

---

### 2. **Try block**

```python
try:
    if flavor not in menu:
        raise InvalidChaiError("that chai is not available")
    if not isinstance(cups, int):
        raise TypeError("Number of cups must be an integer")
```

* Checks two things:

  1. Flavor exists in the menu → if not, raises `InvalidChaiError`.
  2. Cups is an integer → if not, raises `TypeError`.

* If both pass, computes the total bill:

```python
total = menu[flavor] * cups
print(f"Your bill for {cups} cups of {flavor} chai: rupees {total}")
```

---

### 3. **Except block**

```python
except Exception as e:
    print("Error: ", e)
```

* Catches **any exception** (built-in or custom) raised in the `try` block.
* Prints a user-friendly error message.

---

### 4. **Finally block**

```python
finally:
    print("Thank you for visiting chaicode!")
```

* Always runs, regardless of whether an exception occurred.
* Useful for final messages, cleanup, or logging.

---

### 5. **Program flow**

#### Case 1: `"mint", 2`

* `"mint"` is **not in menu** → raises `InvalidChaiError`
  Output:

```
Error:  that chai is not available
Thank you for visiting chaicode!
```

#### Case 2: `"masala", "three"`

* `"masala"` exists → passes first check
* `"three"` is **not an integer** → raises `TypeError`
  Output:

```
Error:  Number of cups must be an integer
Thank you for visiting chaicode!
```

#### Case 3: `"ginger", 3`

* All checks pass → prints total bill
  Output:

```
Your bill for 3 cups of ginger chai: rupees 120
Thank you for visiting chaicode!
```

---

### ✅ Key Takeaways

| Concept              | Explanation                                                          |
| -------------------- | -------------------------------------------------------------------- |
| Custom exception     | `InvalidChaiError` for domain-specific errors                        |
| Built-in exception   | `TypeError` for invalid data types                                   |
| `try-except-finally` | Handle errors gracefully and always execute cleanup/final statements |
| Flow                 | Only one `except` runs for the first raised exception                |

---