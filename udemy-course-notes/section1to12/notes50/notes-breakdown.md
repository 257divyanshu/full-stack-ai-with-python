## ☕ Code Recap

```python
class Chai:
    pass

class ChaiTime:
    pass

print(type(Chai))

ginger_tea = Chai()
print(type(ginger_tea))
print(type(ginger_tea) is Chai)
print(type(ginger_tea) is ChaiTime)
```

---

## 🧩 Step-by-step Explanation

### 1. `class Chai:`

This creates a **class** — a *blueprint* for objects.
Since we used `pass`, it’s currently an *empty class* (no methods or properties yet).

---

### 2. `print(type(Chai))`

This prints the *type* of the class itself.

✅ Output:

```
<class 'type'>
```

Explanation:
In Python, **everything is an object**, including classes.
So the *class `Chai` itself* is an **instance of `type`** (the metaclass that creates all classes).

---

### 3. `ginger_tea = Chai()`

This creates an **instance** (object) of the `Chai` class.

---

### 4. `print(type(ginger_tea))`

✅ Output:

```
<class '__main__.Chai'>
```

This means:
→ `ginger_tea` is an **object** of the class `Chai`.

---

### 5. Type comparisons:

```python
print(type(ginger_tea) is Chai)
```

✅ Output: `True`
→ The object’s type **is exactly** `Chai`.

```python
print(type(ginger_tea) is ChaiTime)
```

✅ Output: `False`
→ `ginger_tea` is **not** an instance of `ChaiTime`.

---

## 🧠 Summary Table

| Expression                     | Meaning                          | Output                    |
| ------------------------------ | -------------------------------- | ------------------------- |
| `type(Chai)`                   | What is `Chai` itself?           | `<class 'type'>`          |
| `type(ginger_tea)`             | What is the instance’s class?    | `<class '__main__.Chai'>` |
| `type(ginger_tea) is Chai`     | Is the instance of class `Chai`? | `True`                    |
| `type(ginger_tea) is ChaiTime` | Is it of class `ChaiTime`?       | `False`                   |

---

💡 **Pro tip:**
Instead of `type(obj) is ClassName`, it’s usually *better* to write:

```python
isinstance(ginger_tea, Chai)
```

This works even with **inheritance** (subclasses), whereas `type(...) is ...` only works for *exact* matches.