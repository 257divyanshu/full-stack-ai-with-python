## ☕ Code Recap

```python
class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"],
        )
    
    @classmethod
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split("-")
        return cls(tea_type, sweetness, size)
    
class ChaiUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ["Small", "Medium", "Large"]


print(ChaiUtils.is_valid_size("Medium"))

order1 = ChaiOrder.from_dict({"tea_type": "masala", "sweetness": "medium", "size":"Large"})
order2 = ChaiOrder.from_string("Ginger-Low-Small")
order3 = ChaiOrder("Large", "Low", "Large")

print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)
```

---

## 🧩 Step-by-step Explanation

### 1. **Instance creation (regular way)**

```python
order3 = ChaiOrder("Large", "Low", "Large")
```

* Directly calls `__init__`.
* Sets `tea_type`, `sweetness`, and `size`.

---

### 2. **`@classmethod` for alternate constructors**

```python
@classmethod
def from_dict(cls, order_data):
    return cls(order_data["tea_type"], order_data["sweetness"], order_data["size"])
```

* Receives `cls` → the class itself (`ChaiOrder` here).
* Lets you create an instance **from a dictionary**.

```python
order1 = ChaiOrder.from_dict({"tea_type": "masala", "sweetness": "medium", "size":"Large"})
```

```python
@classmethod
def from_string(cls, order_string):
    tea_type, sweetness, size = order_string.split("-")
    return cls(tea_type, sweetness, size)
```

* Creates an instance **from a formatted string**.

```python
order2 = ChaiOrder.from_string("Ginger-Low-Small")
```

✅ Both methods are **alternative constructors**, useful for flexible input formats.

---

### 3. **`@staticmethod`**

```python
class ChaiUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ["Small", "Medium", "Large"]
```

* Doesn’t use `self` or `cls`.
* Utility method to **check if a cup size is valid**.

```python
ChaiUtils.is_valid_size("Medium")  # True
```

---

### 4. **Checking object attributes**

```python
print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)
```

Output:

```python
{'tea_type': 'masala', 'sweetness': 'medium', 'size': 'Large'}
{'tea_type': 'Ginger', 'sweetness': 'Low', 'size': 'Small'}
{'tea_type': 'Large', 'sweetness': 'Low', 'size': 'Large'}
```

* `__dict__` shows **all instance attributes** for each order.

---

### 5. **Key Takeaways**

| Concept                | Explanation                                                                 |
| ---------------------- | --------------------------------------------------------------------------- |
| `@classmethod`         | Method receives the class (`cls`) and can create instances in flexible ways |
| `@staticmethod`        | Utility method that doesn’t access instance or class data                   |
| Alternate constructors | `from_dict` and `from_string` allow multiple ways to create objects         |
| Instance attributes    | Stored in `self`, accessible via `__dict__`                                 |

---