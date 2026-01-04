## ☕ Code

```python
chai_menu = {"masala": 30, "ginger": 40}

try:
    chai_menu["elaichi"]
except KeyError:
    print("The key that you are trying to access does not exist")

print("Hello chai code")
```

---

## 🧩 Step-by-step Explanation

### 1. **What is happening?**

```python
chai_menu["elaichi"]
```

* Tries to access a key `"elaichi"` in the dictionary.
* `"elaichi"` **does not exist**, so normally Python would raise a **`KeyError`**.

---

### 2. **Handling the error**

```python
try:
    ...
except KeyError:
    ...
```

* `try` block: place code that might cause an exception.
* `except KeyError`: catch that specific exception and run your handling code.
* Output:

```
The key that you are trying to access does not exist
```

---

### 3. **Code continues**

```python
print("Hello chai code")
```

* Even though a `KeyError` happened, the program **does not crash**.
* Output:

```
Hello chai code
```

---

### ✅ Key Takeaways

| Concept        | Explanation                                             |
| -------------- | ------------------------------------------------------- |
| `try` block    | Code that might raise an exception                      |
| `except` block | Handle a specific exception gracefully                  |
| KeyError       | Raised when accessing a **non-existent dictionary key** |
| Program flow   | Exception handling prevents crashes                     |

---

💡 **Tip:** You can also access dictionary keys safely without exceptions using:

```python
print(chai_menu.get("elaichi", "Not available"))
```

Output:

```
Not available
```