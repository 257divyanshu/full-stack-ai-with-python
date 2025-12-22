## 🧩 What you wrote:

```python
num = 1_000_000_000
print(num)
```

✅ Output:

```
1000000000
```

---

## 💡 Why it prints **without underscores**

The underscores (`_`) in numbers are **just for readability** in your *source code* — they **don’t affect the actual numeric value**.

In other words:

> Underscores in numeric literals are a **visual aid for humans**, ignored by Python when interpreting the number.

---

## 🧠 Python allows underscores in numbers to make large values easier to read.

You can use them anywhere between digits (for clarity):

```python
num = 1_000_000     # one million
price = 12_345.67   # twelve thousand three hundred forty-five point six seven
binary = 0b_1010_1011_0010
hex_num = 0xFF_FF_FF
```

All of these are valid and equivalent to writing the numbers *without* underscores.

---

### ✅ Example:

```python
a = 1_000_000
b = 1000000
print(a == b)  # True
```

Both represent the same integer — **1,000,000**.

---

## 🧮 Why Python removes underscores when printing

When you do:

```python
print(num)
```

Python converts the number back into its **canonical (standard)** string representation — i.e., `1000000000` — with **no formatting characters**.

If you want to keep the visual grouping, you can manually format it:

---

## ✨ Formatting alternatives

### 1️⃣ Use commas for thousands:

```python
print(f"{num:,}")
```

Output:

```
1,000,000,000
```

### 2️⃣ Use underscores in formatted output:

```python
print(f"{num:_}")
```

Output:

```
1_000_000_000
```

So now it prints with underscores — just for display.

---

## ✅ TL;DR

| Concept                                | Explanation                                          |
| -------------------------------------- | ---------------------------------------------------- |
| `_` in numbers                         | Improves readability in code                         |
| Internal meaning                       | Ignored — same as writing without underscores        |
| Print behavior                         | Always prints a plain number (no `_`)                |
| Want underscores/commas when printing? | Use string formatting (`f"{num:_}"` or `f"{num:,}"`) |