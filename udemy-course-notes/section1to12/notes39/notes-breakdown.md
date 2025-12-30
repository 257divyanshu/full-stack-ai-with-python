## 🧩 **Snippet’s Intent**

> To teach how to **filter or transform lists** using **list comprehensions**, instead of writing long loops.

---

### 🧠 Code Explanation

```python
menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger chai"
]
```

* `menu` is a list of different tea options.

---

### 🧩 List comprehension:

```python
iced_tea = [my_tea for my_tea in menu if "Iced" in my_tea]
```

This one line replaces this longer code:

```python
iced_tea = []
for my_tea in menu:
    if "Iced" in my_tea:
        iced_tea.append(my_tea)
```

✅ Breakdown:

* `my_tea for my_tea in menu` → loop through each item
* `if "Iced" in my_tea` → condition to filter only iced teas
* The result is stored in `iced_tea`

---

### 🧾 Output

```python
['Iced Lemon Tea', 'Iced Peach Tea']
```

---

### 🧠 Key Takeaways

| Concept                 | Explanation                                                     |
| ----------------------- | --------------------------------------------------------------- |
| **List comprehension**  | A concise way to build lists                                    |
| **Condition**           | Optional `if` can filter elements                               |
| **Expression**          | First part before `for` defines what to include in the new list |
| **Readable & Pythonic** | Preferred over loops for simple transformations                 |

---

### 🧪 Example Variations

**1️⃣ Without filter**

```python
upper_menu = [tea.upper() for tea in menu]
```

**2️⃣ With condition**

```python
chai_menu = [tea for tea in menu if "Chai" in tea]
```

**3️⃣ With transformation**

```python
tea_lengths = [len(tea) for tea in menu]
```

---