## ☕ Code Recap

```python
class ChaiOrder:
    
    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size}ml of {self.type} chai"
    
order = ChaiOrder("Masala", 200)
print(order.summary())

order_two = ChaiOrder("Ginger", 220)
print(order_two.summary())
```

---

## 🧩 Step-by-step Explanation

### 1. **Constructor (`__init__`)**

```python
def __init__(self, type_, size):
    self.type = type_
    self.size = size
```

* `__init__` is a special method called automatically **when an instance is created**.
* It initializes the **instance attributes** (`self.type` and `self.size`) for that object.
* `type_` and `size` are **parameters passed when creating the instance**.

---

### 2. **Instance method**

```python
def summary(self):
    return f"{self.size}ml of {self.type} chai"
```

* `summary()` uses the instance attributes to give a **description of this order**.
* `self` ensures the method works with the **current instance’s data**.

---

### 3. **Creating instances**

```python
order = ChaiOrder("Masala", 200)
order_two = ChaiOrder("Ginger", 220)
```

* Two separate instances of `ChaiOrder` are created.
* Each has its **own type and size**, independent of the other.

---

### 4. **Calling instance methods**

```python
print(order.summary())       # 200ml of Masala chai
print(order_two.summary())   # 220ml of Ginger chai
```

* Each instance returns a **summary specific to itself**.

---

## 🧠 Key Concepts

| Concept             | Explanation                                               |
| ------------------- | --------------------------------------------------------- |
| `__init__`          | Constructor, called automatically to initialize an object |
| `self`              | Refers to the current instance                            |
| Instance attributes | Stored in `self`, unique to each object                   |
| Instance methods    | Operate on that object’s data                             |

---