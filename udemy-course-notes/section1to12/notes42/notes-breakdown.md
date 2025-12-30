## 🧩 **Snippet’s Intent**

> To show how you can use a **generator expression** with a built-in function (like `sum()`) to quickly process and filter data — in this case, summing only the sales above a certain threshold.

---

### 🧠 Code breakdown

```python
daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]

total_cups = sum(sale for sale in daily_sales if sale > 5)

print(total_cups)
```

---

### 🧾 Step-by-step

1. `daily_sales` → list of chai cups sold per day.

2. Inside `sum()` you have:

   ```python
   (sale for sale in daily_sales if sale > 5)
   ```

   This is a **generator expression** — it works like a list comprehension but doesn’t actually build a list in memory; it generates values one by one (efficiently).

3. The `if sale > 5` filters out smaller sales — only counts sales greater than 5.

4. `sum()` adds them all up.

---

### 🧮 Calculation:

Daily sales above 5: `[10, 12, 7, 8, 9, 15]`
Sum = `10 + 12 + 7 + 8 + 9 + 15 = 61`

✅ Output:

```
61
```

---

### ⚙️ Key Concept — **Generator Expression**

📘 **Syntax:**

```python
(expression for item in iterable if condition)
```

🔹 Unlike list comprehensions `[ ... ]`, generators use `( ... )`.
🔹 They **don’t store data in memory** — instead, they yield values one by one, perfect for large datasets.

---