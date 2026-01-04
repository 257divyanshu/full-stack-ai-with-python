## ☕ Code Recap

```python
# Traditional way with try-finally
# file = open("order.txt", "w")
# try:
#     file.write("Masala chai - 2 cups")
# finally:
#     file.close()


# Modern Pythonic way
with open("order.txt", "w") as file:
    file.write("ginger tea - 4 cups")
```

---

## 🧩 Step-by-step Explanation

### 1. **Old way: `try-finally`**

```python
file = open("order.txt", "w")
try:
    file.write("Masala chai - 2 cups")
finally:
    file.close()
```

* Opens the file in **write mode (`"w"`)**.
* Writes text into it.
* `finally` ensures the file is **always closed**, even if an error occurs while writing.
* Problem: Verbose and easy to forget `finally`.

---

### 2. **Modern way: `with` statement**

```python
with open("order.txt", "w") as file:
    file.write("ginger tea - 4 cups")
```

* `with` automatically handles **opening and closing** the file.
* Even if an error occurs inside the block, Python **closes the file safely**.
* More concise and **Pythonic**.

---

### 3. **Why `with` is better**

* Less boilerplate — no need for explicit `try-finally`.
* Safer — guarantees the file is closed properly.
* Cleaner and easier to read.

---

### ✅ Key Takeaways

| Concept       | Explanation                                              |
| ------------- | -------------------------------------------------------- |
| File modes    | `"w"` → write (overwrites), `"r"` → read, `"a"` → append |
| `try-finally` | Old-school way to ensure file closure                    |
| `with`        | Recommended: automatically manages resources             |
| Safety        | Prevents resource leaks even if errors occur             |

---