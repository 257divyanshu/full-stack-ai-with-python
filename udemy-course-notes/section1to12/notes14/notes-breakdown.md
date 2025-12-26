## 🧩 **Snippet’s Intent:**

> To demonstrate how **boolean variables** work with an `if` statement — and that **nothing prints** unless the condition is `True`.

---

## 🔹 1️⃣ Boolean Variable

```python
kettle_boiled = False
```

✅ **Explanation:**

* A **Boolean** value can be `True` or `False`.
* It often represents a **yes/no** or **on/off** state.
* Here, it tells whether the kettle has finished boiling.

---

## 🔹 2️⃣ Conditional Check

```python
if kettle_boiled:
    print("Kettle Done! time to make Chai")
```

✅ **Explanation:**

* The `if` statement **evaluates the truthiness** of `kettle_boiled`.
* If it’s `True` → the indented block runs.
* If it’s `False` → Python **skips** the block.

✅ Example:

| kettle_boiled | Output                           |
| ------------- | -------------------------------- |
| `True`        | `Kettle Done! time to make Chai` |
| `False`       | *(nothing prints)*               |

---

## 🔹 3️⃣ Teaching Focus

This small file teaches:

* Boolean variables (`True`, `False`)
* How `if` conditions work
* That **no output** occurs if condition is not met

---

## 🧠 Quick Tip

You can flip the value easily:

```python
kettle_boiled = not kettle_boiled
```

Now `False` becomes `True`, and vice versa.

---

## ✅ Summary

| Concept          | Code                    | Purpose                               |
| ---------------- | ----------------------- | ------------------------------------- |
| Boolean variable | `kettle_boiled = False` | Represents on/off or true/false state |
| If condition     | `if kettle_boiled:`     | Checks if value is True               |
| Indentation      | `print(...)`            | Runs only when condition passes       |