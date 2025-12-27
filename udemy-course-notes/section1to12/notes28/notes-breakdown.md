## 🧩 **Snippet’s Intent**

> To teach how **multiple smaller functions** can work together to perform a **bigger task**, and how **functions can call other functions**.

This is a foundational concept in writing **modular, organized, and maintainable code**.

---

### 🧱 1️⃣ Function Definitions

```python
def fetch_sales():
    print("Fetching the sales data")

def filter_valid_sales():
    print("Filtering valid sales data")

def summarize_data():
    print("Summarizing sales data")
```

Each of these defines a **small, focused task**:

* `fetch_sales()` → maybe retrieves raw sales info.
* `filter_valid_sales()` → cleans or validates data.
* `summarize_data()` → compiles totals, averages, etc.

They **don’t return anything yet** — they just print what they’re doing.

---

### 🧮 2️⃣ Higher-level Function

```python
def generate_report():
    fetch_sales()
    filter_valid_sales()
    summarize_data()
    print("Report is ready")
```

Here’s the key idea:

* This function **organizes** the workflow by **calling** the smaller functions in sequence.
* Each call executes the function defined above.
* At the end, it prints `"Report is ready"` — indicating completion.

---

### ▶️ 3️⃣ Function Call

```python
generate_report()
```

When executed:

1. Python looks for `generate_report()`.
2. Runs the code inside it.
3. That code calls the other functions one by one.

✅ **Output:**

```
Fetching the sales data
Filtering valid sales data
Summarizing sales data
Report is ready
```

---

### 🧠 4️⃣ Key Concepts Illustrated

| Concept                               | Explanation                                                |
| ------------------------------------- | ---------------------------------------------------------- |
| **Function composition**              | Building big functionality by combining smaller ones       |
| **Function calling another function** | A function can trigger others inside it                    |
| **Execution flow**                    | The order in which function calls run                      |
| **Code organization**                 | Each function handles one responsibility (SRP principle)   |
| **Main entry point**                  | The last function acts like a “controller” for the process |

---

### ⚙️ 5️⃣ Analogy

Imagine a **tea shop process**:

1. `fetch_sales()` → Collect orders
2. `filter_valid_sales()` → Remove invalid orders
3. `summarize_data()` → Calculate total earnings
4. `generate_report()` → Brings it all together

You don’t need to do everything in one go — each function does **one job well**.

---

### 💡 Bonus Tip

If you later modify how data is fetched or filtered, you only update that **specific function** — not the whole process.
That’s the power of **modular programming**.