## ☕ Code Recap

```python
def brew_chai(flavor):
    if flavor not in ["masala", "ginger", "elaichai"]:
        raise ValueError("Unsupported chai flavor...")
    print(f"brewing {flavor} chai...")

brew_chai("mint")
```

---

## 🧩 Step-by-step Explanation

### 1. **Check the input**

```python
if flavor not in ["masala", "ginger", "elaichai"]:
```

* Ensures the `flavor` is **one of the allowed options**.

---

### 2. **Raise an exception**

```python
raise ValueError("Unsupported chai flavor...")
```

* `raise` immediately **stops execution** of the function.
* Throws a `ValueError` with a **custom message**.
* Python will terminate the program unless the exception is **caught with `try-except`**.

---

### 3. **Valid case**

```python
print(f"brewing {flavor} chai...")
```

* Runs **only if the flavor is valid**.

---

### 4. **Program flow**

* `brew_chai("mint")` → `"mint"` is **not allowed**
* Raises:

```
ValueError: Unsupported chai flavor...
```

---

### ✅ Key Takeaways

| Concept             | Explanation                                         |
| ------------------- | --------------------------------------------------- |
| `raise`             | Used to explicitly trigger an exception             |
| `ValueError`        | Standard Python exception for invalid values        |
| Execution stops     | Code after `raise` in the function **does not run** |
| Catching exceptions | Use `try-except` to handle `raise` safely           |

---

### Example of safe handling

```python
try:
    brew_chai("mint")
except ValueError as e:
    print("Error:", e)
```

Output:

```
Error: Unsupported chai flavor...
```

---