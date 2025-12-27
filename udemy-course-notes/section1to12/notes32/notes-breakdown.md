## 🧩 **Snippet’s Intent**

> To show how variables of the same name can exist at **different levels of scope**, and how Python decides *which one to use*.

---

## 🔤 The LEGB Rule

When Python tries to find a variable, it searches in this order:

| Scope | Meaning                                                        | Example in this file             |
| ----- | -------------------------------------------------------------- | -------------------------------- |
| **L** | **Local** — inside the current function                        | `chai_type` in `serve_chai()`    |
| **E** | **Enclosing** — in the outer (but non-global) function         | `chai_order` in `chai_counter()` |
| **G** | **Global** — declared at top-level in the script               | `chai_order = "Tulsi"`           |
| **B** | **Built-in** — Python’s predefined names (like `print`, `len`) | not used here                    |

---

## 🧩 Part 1: Local vs Global Scope

```python
def serve_chai():
    chai_type = "Masala"  # Local variable
    print(f"Inside function {chai_type}")


chai_type = "Lemon"  # Global variable
serve_chai()
print(f"Outside function: {chai_type}")
```

### 🔍 Step-by-step:

1. The global variable `chai_type` is set to `"Lemon"`.
2. `serve_chai()` defines its own **local** variable `chai_type = "Masala"`.
3. Inside the function, Python uses the **local** one → prints `"Masala"`.
4. Outside, it uses the **global** one → prints `"Lemon"`.

✅ **Output so far:**

```
Inside function Masala
Outside function: Lemon
```

🧠 So, variables with the same name *don’t conflict* — local ones are temporary and exist only inside their function.

---

## 🧩 Part 2: Enclosing Scope (Nested Functions)

```python
def chai_counter():
    chai_order = "lemon"  # Enclosing variable

    def print_order():
        chai_order = "Ginger"  # Local to inner function
        print("Inner:", chai_order)

    print_order()
    print("Outer:", chai_order)


chai_order = "Tulsi"  # Global
chai_counter()
print("Global:", chai_order)
```

### 🔍 Step-by-step:

1. Global variable: `chai_order = "Tulsi"`
2. Outer function `chai_counter()` defines `chai_order = "lemon"` → **enclosing scope**
3. Inner function `print_order()` defines its own `chai_order = "Ginger"` → **local scope**
4. Inside `print_order()`, `"Ginger"` is printed.
5. After returning, the outer function still sees `"lemon"`.
6. Outside everything, the global `"Tulsi"` remains unchanged.

✅ **Output:**

```
Inner: Ginger
Outer: lemon
Global: Tulsi
```

---

## 🧠 What You Learned

| Concept                 | Description                                                                             |
| ----------------------- | --------------------------------------------------------------------------------------- |
| **Local variables**     | Exist only inside the function                                                          |
| **Global variables**    | Available everywhere (unless shadowed)                                                  |
| **Enclosing variables** | Come from an outer function (used in nested defs)                                       |
| **Variable shadowing**  | When a variable with the same name exists in a closer scope, it “shadows” the outer one |

---

### 🔄 Visualization (LEGB Chain)

```
print_order()  → Local: Ginger
                 Enclosing: lemon
                 Global: Tulsi
                 Built-ins: print(), etc.
```

---

### 💡 Bonus Tip

If you ever *want* to modify a global variable inside a function, you must declare it:

```python
def change_global():
    global chai_type
    chai_type = "Cardamom"
```

But in most cases, it's better to **avoid changing globals** — functions should be self-contained.

---

### ✅ Summary Output

Final console output for the entire file:

```
Inside function Masala
Outside function: Lemon
Inner: Ginger
Outer:  lemon
Global : Tulsi
```