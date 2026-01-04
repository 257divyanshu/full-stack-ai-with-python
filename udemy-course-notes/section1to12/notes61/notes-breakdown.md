## ☕ Code

```python
orders = ["masala", "ginger"]

print(orders[2])
```

---

## 🧩 What happens

* `orders` has **2 elements**:

  ```
  Index 0 → "masala"
  Index 1 → "ginger"
  ```

* Python **uses zero-based indexing**, so `orders[2]` refers to the **third element**.

* There is **no third element**, so Python raises:

```
IndexError: list index out of range
```

---

### ✅ Key Takeaways

| Concept                      | Explanation                                           |
| ---------------------------- | ----------------------------------------------------- |
| Indexing                     | Lists start at 0                                      |
| Accessing non-existent index | Raises `IndexError`                                   |
| Safe access                  | Check `len(list)` before indexing or use `try-except` |

---

### Example of safe access

```python
if len(orders) > 2:
    print(orders[2])
else:
    print("No third order available")
```

Output:

```
No third order available
```