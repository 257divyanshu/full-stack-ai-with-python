## 🧩 **Snippet’s Intent**

> To teach:
>
> 1. **Mutable vs immutable objects** and how functions can modify them
> 2. **Positional vs keyword arguments**
> 3. **Arbitrary arguments (`*args` and `**kwargs`)**
> 4. **Default mutable argument pitfalls** and the safe pattern

---

## 1️⃣ Mutable Objects: Lists

```python
chai = [1, 2, 3]

def edit_chai(cup):
    cup[1] = 42

edit_chai(chai)
print(chai)
```

* `chai` is a **list (mutable)**.
* `edit_chai()` changes the **second element** to `42`.
* Lists are **passed by reference**, so the original list is modified.

✅ Output:

```
[1, 42, 3]
```

**Key point:** Mutable objects can be changed inside functions; immutable ones (like strings or ints) cannot.

---

## 2️⃣ Positional vs Keyword Arguments

```python
def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeeling", "Yes", "Low") # positional
make_chai(tea="Green", sugar="Medium", milk="No") # keywords
```

* **Positional arguments** → values assigned by order
* **Keyword arguments** → values assigned by parameter name
* You can mix them but **positional must come first**.

✅ Output:

```
Darjeeling Yes Low
Green No Medium
```

---

## 3️⃣ Arbitrary Arguments (`*args`, `**kwargs`)

```python
def special_chai(*ingredients, **extras):
    print("Ingredients", ingredients)
    print("Extras", extras)

special_chai("Cinnamon", "Cardmom", sweetener="Honey", foam="yes")
```

* `*ingredients` → collects extra **positional arguments** as a tuple
* `**extras` → collects extra **keyword arguments** as a dictionary

✅ Output:

```
Ingredients ('Cinnamon', 'Cardmom')
Extras {'sweetener': 'Honey', 'foam': 'yes'}
```

**Key point:** Use `*args` and `**kwargs` when you don’t know in advance how many arguments will be passed.

---

## 4️⃣ Default Mutable Arguments Pitfall

```python
# Wrong way:
# def chai_order(order=[]):
#     order.append("Masala")
#     print(order)

# Safe way:
def chai_order(order=None):
    if order is None:
        order = []
    print(order)

chai_order()
chai_order()
```

* **Problem:** Default mutable arguments like `[]` persist across calls
* **Solution:** Use `None` and create a new list inside the function
* Here, each call gets a fresh list

✅ Output:

```
[]
[]
```

---

### 🧠 Summary of Concepts

| Concept              | Explanation                                                 |
| -------------------- | ----------------------------------------------------------- |
| Mutable vs Immutable | Lists can be modified inside functions, strings/ints cannot |
| Positional arguments | Assigned by order                                           |
| Keyword arguments    | Assigned by name, order doesn’t matter                      |
| `*args`              | Collect extra positional arguments as a tuple               |
| `**kwargs`           | Collect extra keyword arguments as a dict                   |
| Default mutable args | Avoid using `[]` or `{}` as default; use `None` instead     |

---