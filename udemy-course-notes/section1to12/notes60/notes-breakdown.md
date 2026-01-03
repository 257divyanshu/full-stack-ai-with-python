## ☕ Code Recap

```python
class TeaLeaf:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age + 2
    
    @age.setter
    def age(self, age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Tea leaf age must be between 1 and 5 years")
        
leaf = TeaLeaf(2)
print(leaf.age)
leaf.age = 6
print(leaf.age)
```

---

## 🧩 Step-by-step Explanation

### 1. **Private attribute convention**

```python
self._age = age
```

* Using a single underscore `_age` signals it’s **“internal use”**.
* Users should not modify `_age` directly.

---

### 2. **Getter with `@property`**

```python
@property
def age(self):
    return self._age + 2
```

* `@property` lets you **access `age` like an attribute**:

```python
print(leaf.age)  # Calls the getter automatically
```

* Here, the getter **adds 2 to the stored age**.

---

### 3. **Setter with `@age.setter`**

```python
@age.setter
def age(self, age):
    if 1 <= age <= 5:
        self._age = age
    else:
        raise ValueError("Tea leaf age must be between 1 and 5 years")
```

* Validates **new age values** before storing them.
* Prevents invalid assignments:

```python
leaf.age = 6  # Raises ValueError
```

---

### 4. **Usage**

```python
leaf = TeaLeaf(2)
print(leaf.age)  # 4 (2 + 2)

leaf.age = 6     # ❌ Raises ValueError
```

✅ **Key idea:** You can control **reading and writing** of attributes while still using attribute-like syntax.

---

### 5. **Key Takeaways**

| Concept               | Explanation                                        |
| --------------------- | -------------------------------------------------- |
| `@property`           | Makes a method behave like a readable attribute    |
| `@setter`             | Adds controlled write access to a property         |
| Encapsulation         | Protects internal data (`_age`) and enforces rules |
| Attribute-like syntax | `obj.age` instead of `obj.get_age()`               |

---