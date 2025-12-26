## 🧩 **Snippet’s Intent**

> To teach **nested conditions** — using an `if` inside another `if` — to handle multiple layers of logic.

---

## 🔹 1️⃣ The Setup

```python
device_status = "active"
temperature = 38
```

These are **two separate conditions**:

* `device_status` shows if the device is on or off.
* `temperature` is a numeric value we’ll compare.

---

## 🔹 2️⃣ The Nested Condition

```python
if device_status == "active":
    if temperature > 35:
        print("High temperature alert!")
    else:
        print("Temperature is normal")
else:
    print("Device is offline")
```

Let’s read it logically:

1. **Outer condition:**

   * Check if the device is `"active"`.
   * If not, print `"Device is offline"`.

2. **Inner condition:**

   * If the device *is* active, then check its temperature.
   * If `temperature > 35`, warn user.
   * Otherwise, print normal status.

---

## 🔹 3️⃣ Expected Output

Since:

```python
device_status = "active"
temperature = 38
```

→ The first `if` passes (`active`)
→ The inner `if` also passes (`38 > 35`)

✅ **Output:**

```
High temperature alert!
```

---

## 🔹 4️⃣ What This Teaches

| Concept                       | Meaning                                                 |
| ----------------------------- | ------------------------------------------------------- |
| **Nested if**                 | One `if` inside another for multi-level checks          |
| **Comparison operator (`>`)** | Used to compare numbers                                 |
| **Indentation**               | Defines structure — Python relies on it                 |
| **Control flow**              | Code executes top-to-bottom, skipping irrelevant blocks |

---

## 🧠 Tip

You can sometimes simplify nested logic using **logical operators** like `and`:

```python
if device_status == "active" and temperature > 35:
    print("High temperature alert!")
elif device_status == "active":
    print("Temperature is normal")
else:
    print("Device is offline")
```

This version is shorter but functionally identical.