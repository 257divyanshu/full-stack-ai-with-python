## 🧩 The main topics here are:

### 👉 **Tuple unpacking**,

### 👉 **Multiple assignment / swapping**, and

### 👉 **Membership testing** (`in` keyword).

---
### 🧠 1️⃣ Tuple creation and unpacking

```python
masala_spices = ("cardamom", "cloves", "cinnamon")

(spice1, spice2, spice3) = masala_spices

print(f"Main masala spices: {spice1}, {spice2}, {spice3}")
```

#### 💡 What’s happening:

* `masala_spices` is a **tuple** — an immutable sequence of values.

  ```python
  ("cardamom", "cloves", "cinnamon")
  ```

* The line

  ```python
  (spice1, spice2, spice3) = masala_spices
  ```

  **unpacks** the tuple into individual variables.

So now:

```python
spice1 = "cardamom"
spice2 = "cloves"
spice3 = "cinnamon"
```

When printed:

```
Main masala spices: cardamom, cloves, cinnamon
```

**Tuple unpacking** is a concise way to assign multiple variables at once.

You’ll often see it used for returning multiple values from functions.

---

### 🧠 2️⃣ Multiple assignment and swapping

```python
ginger_ratio, cadramom_ratio = 2, 1
print(f"Ratio is G :{ginger_ratio} and C: {cadramom_ratio}")

ginger_ratio, cadramom_ratio = cadramom_ratio, ginger_ratio
print(f"Ratio is G :{ginger_ratio} and C: {cadramom_ratio}")
```

#### 💡 What’s happening:

* First line: assigns two values at once.

  ```python
  ginger_ratio = 2
  cadramom_ratio = 1
  ```

* Then, this line:

  ```python
  ginger_ratio, cadramom_ratio = cadramom_ratio, ginger_ratio
  ```

  **swaps** the values in one statement — no temporary variable needed!

✅ Output:

```
Ratio is G :2 and C: 1
Ratio is G :1 and C: 2
```

* **Multiple assignment** — assign several variables in a single line.
* **Variable swapping** — a Pythonic, elegant way to exchange values.

---

### 🧠 3️⃣ Membership testing

```python
print(f"Is cinnamon in masala spices ? {'cinnamon' in masala_spices}")
```

#### 💡 What’s happening:

`'cinnamon' in masala_spices` checks whether the value `'cinnamon'` is one of the tuple’s elements.

✅ Output:

```
Is cinnamon in masala spices ? True
```

* **`in` operator** → used to check membership in sequences (tuples, lists, strings, sets, etc.)
* Returns `True` if the item exists, otherwise `False`.

---

## ✅ Summary

| Code Section        | Concept                                                       | Description                              |
| ------------------- | ------------------------------------------------------------- | ---------------------------------------- |
| Tuple unpacking     | `(spice1, spice2, spice3) = masala_spices`                      | Assign multiple values at once           |
| Multiple assignment | `ginger_ratio, cadramom_ratio = 2, 1`                         | Initialize multiple vars cleanly         |
| Swapping            | `ginger_ratio, cadramom_ratio = cadramom_ratio, ginger_ratio` | Swap two values easily                   |
| Membership test     | `'cinnamon' in masala_spices`                                 | Check if an element exists in a sequence |

---

## 💬 In simple terms:

> “This lesson shows how Python handles multiple values — how to unpack them, swap them, and check if a value exists in a group (like a tuple or list).”