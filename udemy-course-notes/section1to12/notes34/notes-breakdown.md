## 🧩 **Snippet’s Intent**

> To teach how **an inner function can modify a global variable** using `global`.
> Shows the difference between `global` and `nonlocal`.

---

### 🧱 1️⃣ Code Analysis

```python
chai_type = "Plain"  # Global variable

def front_desk():
    def kitchen():
        global chai_type
        chai_type = "Irnai"  # Modifies the global variable
    kitchen()
```

* **Global variable**: `chai_type = "Plain"`
* `front_desk()` is an outer function — inside it, `kitchen()` is defined.
* `kitchen()` uses `global chai_type` → this tells Python:

  > “Do **not** create a new local variable; modify the global `chai_type` instead.”
* `kitchen()` sets the global `chai_type` to `"Irnai"`.

---

### 🔁 2️⃣ Step-by-step Execution

1. `front_desk()` is called.
2. Inside `front_desk()`, `kitchen()` is called.
3. `kitchen()` executes:

   * `global chai_type` binds the name to the **top-level variable**
   * `chai_type = "Irnai"` updates the global variable.
4. After returning from both functions, the global variable is now `"Irnai"`.
5. The print statement shows the final global value.

---

### ✅ Output

```
Final global chai:  Irnai
```

Notice:

* The **global variable** was successfully modified by a nested function.
* Contrast this with `nonlocal` (which only affects enclosing function scope, not global).

---

### 🧠 Key Concepts Illustrated

| Concept                        | Explanation                                                                             |
| ------------------------------ | --------------------------------------------------------------------------------------- |
| **Global scope**               | Variable declared at top-level of script                                                |
| **`global` keyword**           | Allows functions to modify global variables                                             |
| **Nested functions**           | Even deeply nested functions can reach globals using `global`                           |
| **Difference from `nonlocal`** | `nonlocal` modifies enclosing function variables; `global` modifies top-level variables |

---

### ⚡ Quick Analogy

* **Global box** = `"Plain"`
* **Kitchen inside front_desk** reaches the global box using `global` → replaces `"Plain"` with `"Irnai"`