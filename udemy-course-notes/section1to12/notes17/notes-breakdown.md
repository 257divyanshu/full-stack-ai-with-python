## 🧩 **Snippet’s Intent**

> To teach **modern, clean alternatives to multiple `if/elif/else` chains** using the `match-case` statement.

---

## 🔹 1️⃣ Getting and normalizing input

```python
seat_type = input("Enter seat type (sleeper/AC/general/luxury)").lower()
```

✅ **Explanation:**

* `input()` gets the user’s choice.
* `.lower()` ensures consistency, e.g., `"AC"` becomes `"ac"` for matching.

---

## 🔹 2️⃣ The `match-case` structure

```python
match seat_type:
    case "sleeper":
        print("Sleeper - No AC, beds available")
    case "ac":
        print("AC - Air conditioned, comfy ride")
    case "general":
        print("General - Cheapest option, no reservation")
    case "luxury":
        print("Luxury - Premium seats with meals")
    case _:
        print("Invalid seat type")
```

✅ **Explanation:**

* `match <variable>` starts a pattern matching block.
* Each `case "<value>"` checks if `seat_type` equals that value.
* `case _:` acts as a **default case**, similar to `else` — catches anything not matched above.

---

## 🔹 3️⃣ Example Outputs

| User Input | Output                           |
| ---------- | -------------------------------- |
| `sleeper`  | Sleeper - No AC, beds available  |
| `ac`       | AC - Air conditioned, comfy ride |
| `vip`      | Invalid seat type                |

---

## 🔹 4️⃣ Concept Being Taught

| Concept                         | Explanation                                                  |
| ------------------------------- | ------------------------------------------------------------ |
| **`match-case`**                | Cleaner alternative to `if/elif/else` chains                 |
| **`case _`**                    | Default case (like `else`)                                   |
| **Input normalization**         | `.lower()` ensures matching works regardless of input case   |
| **Structural pattern matching** | Can match values, types, sequences, and more (advanced uses) |

---

## 🔹 5️⃣ Tip

You could write the same logic with `if-elif-else`, but `match-case`:

* Is more readable when checking **many options**.
* Allows **advanced patterns** in Python 3.10+, like tuples, ranges, or type checks.

Example with `if-elif` equivalent:

```python
if seat_type == "sleeper":
    print("Sleeper - No AC, beds available")
elif seat_type == "ac":
    print("AC - Air conditioned, comfy ride")
...
else:
    print("Invalid seat type")
```