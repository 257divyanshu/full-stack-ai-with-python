## ☕ Code Recap

```python
class Chai:
    origin = "India"

print(Chai.origin)

Chai.is_hot = True
print(Chai.is_hot)

masala = Chai()
print(f"Masala {masala.origin}")
print(f"Masala {masala.is_hot}")
masala.is_hot = False

print("Class: ", Chai.is_hot)
print(f"Masala {masala.is_hot}")
masala.flavor = "Masala"
print(masala.flavor)
```

---

## 🧩 Step-by-step Explanation

### 1. **Class attributes**

```python
class Chai:
    origin = "India"
```

* `origin` is a **class attribute** — shared by all instances unless overridden.

```python
print(Chai.origin)  # India
```

---

### 2. **Adding class attribute dynamically**

```python
Chai.is_hot = True
print(Chai.is_hot)  # True
```

* You can add attributes to the class after it’s defined.
* All instances that don’t have an **instance attribute with the same name** will see this value.

---

### 3. **Creating an instance**

```python
masala = Chai()
print(f"Masala {masala.origin}")   # India
print(f"Masala {masala.is_hot}")  # True
```

* The instance `masala` inherits class attributes by default.

---

### 4. **Overriding instance attribute**

```python
masala.is_hot = False
```

* Now `masala` has its own **instance attribute** `is_hot`.
* It **shadows** the class attribute for this object only.

```python
print("Class: ", Chai.is_hot)        # True
print(f"Masala {masala.is_hot}")     # False
```

---

### 5. **Adding new instance attributes**

```python
masala.flavor = "Masala"
print(masala.flavor)  # Masala
```

* You can create **new attributes** on the fly for individual instances.
* These don’t affect the class or other instances.

---

## 🧠 Key Concepts

| Concept                    | Explanation                                                        |
| -------------------------- | ------------------------------------------------------------------ |
| Class attribute            | Shared by all instances unless overridden                          |
| Instance attribute         | Belongs to a single object; overrides class attribute if same name |
| Dynamic attribute addition | Can add attributes to class or instance after creation             |

---

### ⚡ Example Analogy

Think of `Chai` as a tea **blueprint**:

* `origin = "India"` → every chai comes from India by default.
* `is_hot = True` → all chai are hot unless you override for a cup.
* `masala.flavor = "Masala"` → only this specific cup has Masala flavor.