## ☕ Code Recap

```python
class Chai:
    temperature = "hot"
    strength = "Strong"

cutting = Chai()
print(cutting.temperature)

cutting.temperature = "Mild"
cutting.cup = "small"
print("After changing ", cutting.temperature)
print("cup size is  ", cutting.cup)
print("Direct look into the class ", Chai.temperature)

del cutting.temperature
del cutting.cup
print(cutting.temperature)
print(cutting.cup)
```

---

## 🧩 Step-by-step Explanation

### 1. **Class attributes**

```python
class Chai:
    temperature = "hot"
    strength = "Strong"
```

* `temperature` and `strength` are **class attributes** — shared by all instances by default.

```python
cutting = Chai()
print(cutting.temperature)  # hot
```

---

### 2. **Overriding / adding instance attributes**

```python
cutting.temperature = "Mild"
cutting.cup = "small"
```

* `cutting.temperature` now becomes an **instance attribute**, which **shadows** the class attribute `temperature`.
* `cutting.cup` is a new instance attribute (does not exist on the class).

```python
print("After changing ", cutting.temperature)  # Mild
print("cup size is  ", cutting.cup)           # small
print("Direct look into the class ", Chai.temperature)  # hot
```

✅ Observation:

* Changing the instance attribute **does not affect the class attribute**.

---

### 3. **Deleting attributes**

```python
del cutting.temperature
del cutting.cup
```

* `del cutting.temperature` removes the **instance attribute** only.
* Now, if we access `cutting.temperature`, Python falls back to the **class attribute**.

```python
print(cutting.temperature)  # hot
```

* `del cutting.cup` removes the instance attribute.
* `cup` was only an instance attribute, so after deletion it **no longer exists**:

```python
print(cutting.cup)  # Raises AttributeError (since it doesn’t exist)
```

---

## 🧠 Key Concepts

| Concept                    | Explanation                                                                                         |
| -------------------------- | --------------------------------------------------------------------------------------------------- |
| Shadowing                  | Instance attribute overrides a class attribute of the same name                                     |
| Dynamic attribute addition | You can add new attributes to instances at any time                                                 |
| `del`                      | Deletes an attribute; if a class attribute is deleted from the instance, access falls back to class |

---
