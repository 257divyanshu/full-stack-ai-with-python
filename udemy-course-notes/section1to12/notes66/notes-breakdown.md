## ☕ Code Recap

```python
class OutOfIngredientsError(Exception):
    pass

def make_chai(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngredientsError("Missing milk or sugar")
    print("chai is ready...")

make_chai(0, 1)
```

---

## 🧩 Step-by-step Explanation

### 1. **Custom Exception**

```python
class OutOfIngredientsError(Exception):
    pass
```

* Inherits from Python’s built-in `Exception` class.
* Lets you **create a specific type of error** for your domain.
* `pass` means no extra behavior — it’s just a named exception.

---

### 2. **Raise the custom exception**

```python
if milk == 0 or sugar == 0:
    raise OutOfIngredientsError("Missing milk or sugar")
```

* Checks for missing ingredients.
* If **milk or sugar is zero**, it raises `OutOfIngredientsError` with a **custom message**.

---

### 3. **Program flow**

```python
make_chai(0, 1)
```

* `milk = 0`, `sugar = 1` → condition is True.
* Python raises:

```
__main__.OutOfIngredientsError: Missing milk or sugar
```

* Execution stops unless **caught in a `try-except` block**.

---

### 4. **Catching the custom exception**

```python
try:
    make_chai(0, 1)
except OutOfIngredientsError as e:
    print("Error:", e)
```

Output:

```
Error: Missing milk or sugar
```

---

### ✅ Key Takeaways

| Concept                  | Explanation                                       |
| ------------------------ | ------------------------------------------------- |
| Custom exception         | Create domain-specific errors for clarity         |
| Inherit from `Exception` | Standard way to define new exceptions             |
| `raise`                  | Trigger your custom error when a condition occurs |
| Catch it                 | Use `try-except` just like built-in exceptions    |

---