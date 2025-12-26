## 🧩 **Snippet’s Intent**

> To demonstrate the **Walrus operator (`:=`)** — assigning and testing a value **in a single expression**.

---

## 🔹 1️⃣ The setup

```python
value = 13

if remainder := value % 5:
    print(f"Not divisible, remainder is {remainder}")
```

✅ **What’s happening:**

* `value % 5` → computes the remainder (here, `3`)
* `remainder := value % 5` → assigns **3 to remainder** *and returns 3* (truthy)
* `if remainder:` → condition is True, so it prints:

```
Not divisible, remainder is 3
```

---

### 🧠 Normally (without :=)

```python
remainder = value % 5
if remainder:
    print(f"Not divisible, remainder is {remainder}")
```

Both mean the same —
but the Walrus operator combines **assignment + check** in one step.

---

## 🔹 2️⃣ Another Example (commented part)

```python
available_sizes = ["small", "medium", "large"]

if (requested_size := input("Enter your chai cup size: ")) in available_sizes:
    print(f"Serving {requested_size} chai")
else:
    print(f"Size is unavailable - {requested_size}")
```

✅ **Here’s what’s cool:**

* `(requested_size := input(...))` assigns user input to `requested_size`
* Immediately checks if it’s in the list `available_sizes`
* No need for two separate lines

So if you enter `"medium"` →
Output:

```
Serving medium chai
```

---

## 🔹 3️⃣ Realtime input loop (practical use)

```python
flavors = ["masala", "ginger", "lemon", "mint"]

print("Available flavors: ", flavors)

while (flavor := input("Choose your flavor: ")) not in flavors:
    print(f"Sorry, {flavor} is not available")

print(f"You choose {flavor} chai")
```

### ✅ What happens:

* The user is repeatedly prompted for input.
* `flavor := input(...)` assigns input and checks it at the same time.
* The loop continues **until** the entered `flavor` is found in the list.

Example run:

```
Available flavors:  ['masala', 'ginger', 'lemon', 'mint']
Choose your flavor: vanilla
Sorry, vanilla is not available
Choose your flavor: ginger
You choose ginger chai
```

---

## 🔹 4️⃣ Summary Table

| Operator         | Meaning                                                        |
| ---------------- | -------------------------------------------------------------- |
| `=`              | Simple assignment (statement)                                  |
| `:=`             | Assignment **inside** an expression (expression + value check) |
| Introduced in    | **Python 3.8+**                                                |
| Common use cases | Loops, conditions, data processing                             |

---

## 🔹 5️⃣ Analogy

🗣️ “Let’s both **store** the answer **and check it immediately**.”

Instead of:

> “Compute it first. Then check it.”

We do both in one smooth line.

---

## 🧾 **Key Learnings from this file**

* Using `:=` (Walrus operator) in `if` and `while`
* Cleaner and more concise syntax
* Practical input validation loops
* Understanding truthy/falsy remainders