## ☕ Code Recap

```python
class A:
    label = "A: Base class"

class B(A):
    label = "B: Masala blend"

class C(A):
    label = "C: Herbal blend"

class D(C, B):
    pass

cup = D()
print(cup.label)
print(D.__mro__)
```

---

## 🧩 Step-by-step Explanation

### 1. **Class hierarchy**

```
      A
     / \
    B   C
     \ /
      D
```

* `B` and `C` inherit from `A`.
* `D` inherits from **C first, then B**.

---

### 2. **Accessing `label`**

```python
cup = D()
print(cup.label)
```

* Python looks for `label` **following the MRO** (Method Resolution Order).
* `D` → `C` → `B` → `A`
* First `label` found: **`C: Herbal blend`** ✅

---

### 3. **MRO (Method Resolution Order)**

```python
print(D.__mro__)
```

* Shows the order Python checks for attributes/methods:

```
(<class '__main__.D'>,
 <class '__main__.C'>,
 <class '__main__.B'>,
 <class '__main__.A'>,
 <class 'object'>)
```

* Python uses **C3 linearization algorithm** to determine MRO in multiple inheritance.

---

### 4. **Key Takeaways**

| Concept              | Explanation                                               |
| -------------------- | --------------------------------------------------------- |
| Multiple inheritance | A class can inherit from more than one parent (`D(C, B)`) |
| MRO                  | Order in which Python searches for attributes/methods     |
| Attribute lookup     | Python stops at the **first occurrence** in MRO           |

---