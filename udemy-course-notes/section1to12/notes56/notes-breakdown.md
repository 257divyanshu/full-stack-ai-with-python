## ☕ Code Recap
 
```python
class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength

# Three ways to define GingerChai (two commented out)

# Using super() to call parent constructor
class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)
        self.spice_level = spice_level
```

---

## 🧩 Step-by-step Explanation

### 1. **Base class `Chai`**

```python
class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength
```

* Base class for all teas.
* `__init__` sets **type** and **strength**.

---

### 2. **Subclass `GingerChai`**

```python
class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)
        self.spice_level = spice_level
```

* `GingerChai` inherits from `Chai`.
* Adds a new attribute: `spice_level`.

---

### 3. **Calling the parent constructor**

**Three approaches:**

#### a) Wrong way (not calling parent):

```python
# self.type = type_
# self.strength = strength
# self.spice_level = spice_level
```

* Works, but duplicates code from the parent class.
* Not ideal — violates DRY principle.

#### b) Explicit call using class name:

```python
# Chai.__init__(self, type_, strength)
# self.spice_level = spice_level
```

* Works, manually calls parent constructor.
* Slightly verbose and less flexible if class hierarchy changes.

#### c) Recommended: `super()`

```python
super().__init__(type_, strength)
self.spice_level = spice_level
```

* Calls the parent class’s `__init__` automatically.
* Cleaner, handles inheritance better if the base class changes.
* `super()` always refers to the next class in the **MRO (Method Resolution Order)**.

---

### 4. **Usage Example**

```python
ginger = GingerChai("Ginger", "Strong", "High")
print(ginger.type)         # Ginger
print(ginger.strength)     # Strong
print(ginger.spice_level)  # High
```

* `type` and `strength` come from **base class**.
* `spice_level` comes from **subclass**.

---

## 🧠 Key Concepts

| Concept               | Explanation                                                                   |
| --------------------- | ----------------------------------------------------------------------------- |
| Inheritance           | Subclass gets attributes and methods from parent class                        |
| `super()`             | Calls parent method dynamically, cleaner than `ParentClass.method(self, ...)` |
| Extending constructor | Subclass adds new attributes while reusing parent initialization              |

---

💡 **Tip:** Always use `super().__init__()` in modern Python — it avoids potential errors in complex multiple inheritance scenarios.