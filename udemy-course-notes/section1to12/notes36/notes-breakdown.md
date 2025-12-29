## 🧩 **Snippet’s Intent**

> To teach:
>
> 1. The difference between functions that **return** vs **just print**
> 2. Functions that **return `None`**
> 3. **Conditional returns**
> 4. **Returning multiple values (tuples)**

---

## 1️⃣ Functions that only print vs functions that return

```python
def make_chai():
    print("Here is your masala chai")

return_value = make_chai()
print(return_value)
```

* `make_chai()` **only prints**, it does **not return anything**.
* Functions that don’t have a `return` statement automatically return `None`.

✅ Output:

```
Here is your masala chai
None
```

* This teaches: **printing vs returning are different**.

  * Printing → just shows output
  * Returning → passes value back to the caller

---

## 2️⃣ Function with `pass`

```python
def idle_chaiwala():
    pass

print(idle_chaiwala())
```

* `pass` → placeholder, does nothing
* Function returns `None` by default

✅ Output:

```
None
```

---

## 3️⃣ Function that returns a single value

```python
def sold_cups():
    return 120

total = sold_cups()
print(total)
```

* `sold_cups()` **returns** 120
* Stored in `total` → printed

✅ Output:

```
120
```

---

## 4️⃣ Conditional return

```python
def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry, chai over"
    return "Chai is ready"
    print("chai")  # this never executes
```

* Only **one branch executes**, function exits immediately after `return`
* `print("chai")` after `return` is **dead code**, never runs

✅ Output:

```python
chai_status(0) → "Sorry, chai over"
chai_status(5) → "Chai is ready"
```

---

## 5️⃣ Returning multiple values

```python
def chai_report():
    return 100, 20, 10  # sold, remaining, not_paid

sold, remaining, not_paid = chai_report()
print("Sold: ", sold)
print("Remaining: ", remaining)
```

* Python automatically packs multiple values into a **tuple** `(100, 20, 10)`
* You can **unpack** them into separate variables
* Very useful for returning **multiple results** from a function

✅ Output:

```
Sold: 100
Remaining: 20
```

---

### 🧠 Key Concepts Illustrated

| Concept                       | Explanation                                             |
| ----------------------------- | ------------------------------------------------------- |
| **`return` vs `print`**       | `print` shows output, `return` passes it back           |
| **No return → None**          | Functions without `return` return `None` automatically  |
| **Conditional return**        | Function exits immediately when `return` is executed    |
| **Returning multiple values** | Python packs them as a tuple, can unpack when receiving |