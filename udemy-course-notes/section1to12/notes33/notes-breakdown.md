## 🧩 **Snippet’s Intent**

> To teach how **nested functions** can modify variables in their **enclosing (but non-global) scope** using `nonlocal`.

---

### 🧱 1️⃣ Code Analysis

```python
chai_type = "ginger"  # Global variable

def update_order():
    chai_type = "Elaichi"  # Enclosing variable for kitchen()

    def kitchen():
        nonlocal chai_type
        chai_type = "Kesar"  # Updates the enclosing variable

    kitchen()
    print("After kitchen update", chai_type)
```

* **Global `chai_type`** = `"ginger"` → not touched in this example.
* `update_order()` defines **`chai_type` = "Elaichi"`** → this is in the **enclosing scope** for `kitchen()`.
* `kitchen()` uses `nonlocal chai_type` → it tells Python:

  > “Don’t create a new local variable; modify the one in the enclosing function (`update_order`)”

---

### 🔁 2️⃣ Step-by-step Execution

1. `update_order()` is called.
2. Inside `update_order()`, `chai_type = "Elaichi"` is created (enclosing variable for inner function).
3. `kitchen()` is called:

   * `nonlocal chai_type` binds it to the enclosing variable
   * `chai_type = "Kesar"` updates the **enclosing variable**
4. After returning from `kitchen()`, the enclosing variable in `update_order()` is now `"Kesar"`.
5. The print statement inside `update_order()` shows the updated value.

---

### ✅ Output

```
After kitchen update Kesar
```

Notice:

* The **global variable** `"ginger"` is unchanged.
* Only the **enclosing variable** (`update_order()`’s `chai_type`) is modified.

---

### 🧠 Key Concepts Illustrated

| Concept                      | Explanation                                                                             |
| ---------------------------- | --------------------------------------------------------------------------------------- |
| **Local scope**              | Variables inside a function (`kitchen` local variables)                                 |
| **Enclosing scope**          | Variables in the outer (enclosing) function (`update_order`)                            |
| **Global scope**             | Top-level variable `chai_type = "ginger"`                                               |
| **`nonlocal` keyword**       | Lets inner function modify a variable in its enclosing scope                            |
| **Difference from `global`** | `global` modifies top-level variables, `nonlocal` modifies enclosing function variables |

---

### ⚡ Quick Analogy

Think of it as **nested boxes**:

```
Global box: "ginger"
└─ Enclosing box (update_order): "Elaichi" → kitchen can reach this via `nonlocal`
    └─ Local box (kitchen): modifies enclosing box
```

After `kitchen()` runs, the **enclosing box** now has `"Kesar"`.