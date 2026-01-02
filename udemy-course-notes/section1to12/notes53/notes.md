## ☕ Code Recap

```python
class Chaicup:
    size = 150  # ml

    def describe(self):
        return f"A {self.size}ml chai cup"
    
cup = Chaicup()
print(cup.describe())
print(Chaicup.describe(cup))

cup_two = Chaicup()
cup_two.size = 100
print(Chaicup.describe(cup_two))
```

---

## 🧩 Step-by-step Explanation

### 1. **Class attribute**

```python
size = 150
```

* `size` is a **class attribute**, shared by all instances unless overridden.

---

### 2. **Instance method**

```python
def describe(self):
    return f"A {self.size}ml chai cup"
```

* `describe` is a **method** of the class.
* `self` refers to the **specific instance** calling the method.
* Accessing `self.size` first looks for an **instance attribute**.
  If not found, it falls back to the **class attribute**.

---

### 3. **Calling the method via instance**

```python
cup = Chaicup()
print(cup.describe())  # A 150ml chai cup
```

* `cup` has no instance attribute `size`, so it uses the class attribute `Chaicup.size`.

---

### 4. **Calling the method via class**

```python
print(Chaicup.describe(cup))  # A 150ml chai cup
```

* Equivalent to `cup.describe()`.
* You must **pass the instance explicitly** when calling via the class.

---

### 5. **Overriding instance attribute**

```python
cup_two = Chaicup()
cup_two.size = 100
print(Chaicup.describe(cup_two))  # A 100ml chai cup
```

* Here, `cup_two` has an **instance attribute** `size = 100`.
* `self.size` now refers to the **instance attribute**, shadowing the class attribute.

---

## 🧠 Key Concepts

| Concept               | Explanation                                                        |
| --------------------- | ------------------------------------------------------------------ |
| Class attribute       | Shared by all instances unless shadowed                            |
| Instance attribute    | Specific to that object; overrides class attribute if name matches |
| `self`                | Refers to the current instance of the class                        |
| Method call via class | Must pass instance explicitly: `Class.method(instance)`            |

---