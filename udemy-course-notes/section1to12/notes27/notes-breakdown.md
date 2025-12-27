## 🧩 **Snippet’s Intent**

> To teach how to **define reusable code blocks using functions** — with **parameters** and **function calls**.

---

### 🧱 1️⃣ Defining a Function

```python
def print_order(name, chai_type):
    print(f"{name} ordered {chai_type} chai!")
```

* `def` → keyword that defines a function.
* `print_order` → name of the function.
* `(name, chai_type)` → parameters (placeholders for input values).
* Code inside the function runs **only when the function is called**.

---

### 🧮 2️⃣ Calling the Function

```python
print_order("Aman", "masala")
print_order("Hitesh", "Ginger")
print_order("Jia", "Tulsi")
```

Here:

* `"Aman"`, `"Hitesh"`, `"Jia"` → values passed for the `name` parameter.
* `"masala"`, `"Ginger"`, `"Tulsi"` → values passed for the `chai_type` parameter.

Each call executes the print statement inside the function.

✅ **Output:**

```
Aman ordered masala chai!
Hitesh ordered Ginger chai!
Jia ordered Tulsi chai!
```

---

### 🔹 3️⃣ Key Concepts Illustrated

| Concept                 | Explanation                                                   |
| ----------------------- | ------------------------------------------------------------- |
| **Function Definition** | `def function_name(parameters):` defines reusable logic       |
| **Parameters**          | Variables that receive input when function is called          |
| **Function Call**       | Executes the code inside the function with specific arguments |
| **Code Reuse**          | You can call the same logic many times with different values  |
| **f-strings**           | Used to neatly combine variables and text                     |

---

### 🧠 Analogy

Think of a function like a **recipe** — you define how to make chai once (the steps), and then **reuse it** for any flavor or customer name by giving it different ingredients (arguments).

---

### 💡 Bonus Tip

You can even give **default values** to parameters, like:

```python
def print_order(name, chai_type="Masala"):
    print(f"{name} ordered {chai_type} chai!")
```

Now if you call:

```python
print_order("Aman")
```

Output will be:

```
Aman ordered Masala chai!
```