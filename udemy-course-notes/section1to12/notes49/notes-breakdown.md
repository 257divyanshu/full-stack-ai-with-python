## ☕ Code Recap

```python
from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied: Admins only")
            return None
        else:
            return func(user_role)
    return wrapper

@require_admin
def acess_tea_inventory(role):
    print("Access granted to tea inventory")

acess_tea_inventory("user")
acess_tea_inventory("admin")
```

---

## 🧩 Step-by-step explanation

### 1. The decorator `require_admin`

It takes a function (like `acess_tea_inventory`) and wraps it inside `wrapper()`.

Inside `wrapper()`:

* It checks if the incoming argument `user_role` equals `"admin"`.
* If **not**, it prints an access-denied message and stops execution.
* If **yes**, it calls the real function `func(user_role)`.

---

### 2. Decoration process

This line:

```python
@require_admin
def acess_tea_inventory(role):
```

is equivalent to:

```python
acess_tea_inventory = require_admin(acess_tea_inventory)
```

So now, calling `acess_tea_inventory()` will automatically go through the `wrapper()` logic first.

---

### 3. Execution

**Case 1:**

```python
acess_tea_inventory("user")
```

* `wrapper("user")` runs
* `user_role != "admin"` → True
  ✅ Output:

```
Access denied: Admins only
```

**Case 2:**

```python
acess_tea_inventory("admin")
```

* `wrapper("admin")` runs
* `user_role == "admin"` → True
* Calls real function → prints:

```
Access granted to tea inventory
```

---

## 🧠 Why this matters

This is a **real-world pattern** in backend apps (Flask, Django, FastAPI, etc.) where decorators control who can access what.

| Concept           | Meaning                                        |
| ----------------- | ---------------------------------------------- |
| `@wraps(func)`    | Keeps original function metadata               |
| Conditional check | Validates user permissions                     |
| Decorator         | Adds logic **before** the target function runs |

---

💡 **Pro tip:**
If you want this decorator to handle *any* function (not just ones with a single argument), you can generalize it like this:

```python
def require_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        role = kwargs.get("role") or (args[0] if args else None)
        if role != "admin":
            print("Access denied: Admins only")
            return None
        return func(*args, **kwargs)
    return wrapper
```

That way, it’ll work even if the function has more parameters or uses keyword arguments.