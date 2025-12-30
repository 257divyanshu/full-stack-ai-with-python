## 🧩 **Snippet’s Intent**

> To teach how to use **dictionary comprehensions** to create or transform key–value pairs in one line.

---

### 🧠 Code breakdown

```python
tea_prices_inr = {
    "Masala Chai": 40,
    "Green Tea": 50,
    "Lemon Tea": 200
}

tea_prices_usd = {tea: price / 80 for tea, price in tea_prices_inr.items()}
print(tea_prices_usd)
```

---

### 🧾 Step-by-step Explanation

1. `tea_prices_inr.items()` → returns pairs like:

   ```
   ("Masala Chai", 40)
   ("Green Tea", 50)
   ("Lemon Tea", 200)
   ```
2. `for tea, price in tea_prices_inr.items()` → iterates over those pairs.
3. `tea: price / 80` → creates a new key–value pair where:

   * key → same tea name
   * value → converted to USD (divided by 80)
4. `{ ... for ... }` → builds a **new dictionary** with the converted prices.

---

### 🧮 Output:

```
{'Masala Chai': 0.5, 'Green Tea': 0.625, 'Lemon Tea': 2.5}
```

---

### 🧠 Key Concept — Dictionary Comprehension

📘 **Syntax:**

```python
{key_expression: value_expression for item in iterable if condition}
```

You can even filter or transform data easily:

```python
expensive_teas = {tea: price for tea, price in tea_prices_inr.items() if price > 100}
```

✅ Output:

```
{'Lemon Tea': 200}
```

---