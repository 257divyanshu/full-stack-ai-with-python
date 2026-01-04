## ☕ Code Recap

```python
def serve_chai(flavor):
    try:
        print(f"Preparing {flavor} chai...")
        if flavor == "unknown":
            raise ValueError("We don't know that flavor")
    except ValueError as e:
        print("Error: ", e)
    else:
        print(f"{flavor} chai is served")
    finally:
        print("Next customer please")

serve_chai("masala")
serve_chai("unknown")
```

---

## 🧩 Step-by-step Explanation

### 1. **`try` block**

```python
try:
    print(f"Preparing {flavor} chai...")
    if flavor == "unknown":
        raise ValueError("We don't know that flavor")
```

* Contains code that **might raise an exception**.
* Here, we explicitly raise a `ValueError` if the flavor is `"unknown"`.

---

### 2. **`except` block**

```python
except ValueError as e:
    print("Error: ", e)
```

* Catches the `ValueError` and prints the error message.
* Only runs **if an exception occurs**.

---

### 3. **`else` block**

```python
else:
    print(f"{flavor} chai is served")
```

* Runs **only if no exception occurs** in the `try` block.
* So, for valid flavors like `"masala"`, this executes.

---

### 4. **`finally` block**

```python
finally:
    print("Next customer please")
```

* Always runs **regardless of whether an exception occurred or not**.
* Useful for cleanup actions, like closing a connection or serving the next customer.

---

### 5. **Program flow**

#### Case 1: `"masala"`

```
Preparing masala chai...
masala chai is served
Next customer please
```

#### Case 2: `"unknown"`

```
Preparing unknown chai...
Error:  We don't know that flavor
Next customer please
```

---

### ✅ Key Takeaways

| Concept            | Explanation                                     |
| ------------------ | ----------------------------------------------- |
| `try`              | Code that might fail                            |
| `except`           | Handle the error                                |
| `else`             | Runs only if **no error**                       |
| `finally`          | Runs **always**, for cleanup or final steps     |
| Raising exceptions | `raise ValueError("message")` signals a problem |

---