## ☕ Code Recap
 
```python
class ChaiUtils:
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]
    
raw = " water , milk , ginger , honey "
cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)
```

---

## 🧩 Step-by-step Explanation

### 1. **What is `@staticmethod`?**

* `@staticmethod` decorates a method **inside a class** but:

  * It **does not receive `self`** (no instance reference)
  * It **does not receive `cls`** (no class reference)
* Essentially, it behaves like a **regular function**, just namespaced in the class.

---

### 2. **Why use it here?**

```python
def clean_ingredients(text):
    return [item.strip() for item in text.split(",")]
```

* Cleans up a comma-separated string by removing extra spaces.
* We don’t need **any instance or class attributes**, so it’s perfect as a `staticmethod`.

---

### 3. **Calling a static method**

```python
cleaned = ChaiUtils.clean_ingredients(raw)
```

* Call directly from the class, no instance needed.
* Output:

```python
['water', 'milk', 'ginger', 'honey']
```

---

### 4. **Key Points**

| Concept         | Explanation                                                     |
| --------------- | --------------------------------------------------------------- |
| `@staticmethod` | Method inside a class that **doesn’t use `self` or `cls`**      |
| Use case        | Group related utility functions inside a class for organization |
| Call            | `ClassName.method()` or `instance.method()`                     |

---