## 🧩 **Snippet’s Intent:**

> To demonstrate how to take **user input**, normalize it (using `.lower()`), and use **conditional statements (`if / elif / else`)** to make decisions based on that input.

---

## 🔹 1️⃣ Getting user input

```python
cup = input("Choose your cup size (small/medium/large): ").lower()
```

✅ **Explanation:**

* `input()` → pauses the program and waits for user input from the keyboard.
* Whatever the user types is captured as a **string**.
* `.lower()` converts it to **lowercase**, so `"SMALL"` or `"Small"` both become `"small"` — avoiding case mismatches.

✅ Example:

```
Choose your cup size (small/medium/large): Medium
```

→ `cup` will be `"medium"`

🧩 **Concept taught:**
→ How to accept and standardize **user input**.

---

## 🔹 2️⃣ Conditional logic (`if / elif / else`)

```python
if cup == "small":
    print("Price is 10 rupees")
elif cup == "medium":
    print("Price is 15 rupees")
elif cup == "large":
    print("price is 20 rupees")
else:
    print("Unknown cup size")
```

✅ **Explanation:**

* The program checks each condition **in order**:

  * If the cup size is `"small"`, it prints 10 rupees.
  * Else if `"medium"`, prints 15 rupees.
  * Else if `"large"`, prints 20 rupees.
  * If none match → the `else` block handles any unexpected input.

✅ Example Outputs:

```
Price is 10 rupees
```

or

```
Unknown cup size
```

🧩 **Concept taught:**
→ How to perform **branching** — executing different code paths based on conditions.

---

## ✅ Summary Table

| Concept        | Code               | Explanation                               |
| -------------- | ------------------ | ----------------------------------------- |
| Get user input | `input("...")`     | Waits for keyboard input                  |
| Normalize text | `.lower()`         | Makes text lowercase to avoid case issues |
| Conditional    | `if / elif / else` | Choose code branch based on condition     |
| Equality check | `==`               | Compares two values                       |

---

## 🧠 Key Takeaways

* Use `input()` to make interactive programs.
* Use `.lower()` or `.strip()` to clean user input.
* Conditional statements let your program **make decisions** dynamically.
* Always include an `else` to handle unexpected inputs gracefully.