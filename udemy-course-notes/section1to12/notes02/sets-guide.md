## 🧩 What is a Set in Python?

A **set** is an **unordered collection of unique elements**.

Think of it like a **mathematical set**:

> “A bag of distinct things — no duplicates, and order doesn’t matter.”

---

## 🧱 Creating a Set

```python
# Using curly braces
numbers = {1, 2, 3, 4}

# Or using the set() constructor
letters = set(['a', 'b', 'c'])
```

✅ Output:

```python
{1, 2, 3, 4}
{'a', 'b', 'c'}
```

⚠️ Empty set:

```python
empty = set()   # ✅ Correct
empty = {}      # ❌ Creates an empty dict, not a set
```

---

## 🧠 Key Characteristics

| Property                       | Description                                             |
| ------------------------------ | ------------------------------------------------------- |
| **Unordered**                  | The elements have no fixed position or index            |
| **Unindexed**                  | You can’t access elements by position (like `myset[0]`) |
| **Unique elements**            | Duplicates are automatically removed                    |
| **Mutable**                    | You can add or remove elements after creation           |
| **Elements must be immutable** | (e.g. numbers, strings, tuples) but not lists or dicts  |

---

## 🎯 Example: Duplicates get removed

```python
s = {1, 2, 2, 3, 3, 3}
print(s)
```

➡️ Output:

```
{1, 2, 3}
```

---

## ⚙️ Common Set Operations

### 🧩 Add elements

```python
s = {1, 2, 3}
s.add(4)
print(s)
# {1, 2, 3, 4}
```

### 🧩 Remove elements

```python
s.remove(2)   # removes 2, raises error if not found
s.discard(5)  # removes 5 if present, does nothing if not
```

### 🧩 Pop an element (randomly)

```python
s.pop()
```

### 🧩 Clear all elements

```python
s.clear()
```

---

## 🧮 Mathematical Set Operations

### 🔹 Union (`|` or `.union()`)

Combine two sets (unique elements only):

```python
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)           # {1, 2, 3, 4, 5}
print(a.union(b))      # same result
```

### 🔹 Intersection (`&` or `.intersection()`)

Common elements in both:

```python
print(a & b)           # {3}
print(a.intersection(b))
```

### 🔹 Difference (`-` or `.difference()`)

Elements in `a` but not in `b`:

```python
print(a - b)           # {1, 2}
```

### 🔹 Symmetric Difference (`^` or `.symmetric_difference()`)

Elements in *either* set, but not both:

```python
print(a ^ b)           # {1, 2, 4, 5}
```

---

## 🔍 Checking relationships between sets

```python
a = {1, 2, 3}
b = {1, 2}
```

| Operation         | Meaning                     | Result  |
| ----------------- | --------------------------- | ------- |
| `b.issubset(a)`   | Are all elements of b in a? | ✅ True  |
| `a.issuperset(b)` | Does a contain all of b?    | ✅ True  |
| `a.isdisjoint(b)` | Do they share no elements?  | ❌ False |

---

## ⚡ Real-world examples

### 1️⃣ Removing duplicates from a list

```python
nums = [1, 2, 2, 3, 3, 4]
unique_nums = set(nums)
print(unique_nums)
# {1, 2, 3, 4}
```

### 2️⃣ Fast membership checking

```python
names = {"Alice", "Bob", "Charlie"}
print("Bob" in names)   # True
```

✅ Much faster than checking inside a list for large collections.

### 3️⃣ Comparing tags or categories

```python
skills_a = {"python", "sql", "git"}
skills_b = {"python", "react"}

common = skills_a & skills_b
print(common)  # {'python'}
```

---

## 🧱 Frozenset (the immutable cousin)

If you want a set that **can’t be modified**, use:

```python
f = frozenset([1, 2, 3])
```

You can perform union/intersection operations, but not add/remove items.

---

## ✅ Summary Table

| Operation      | Symbol | Method                    | Description              |                     |
| -------------- | ------ | ------------------------- | ------------------------ | ------------------- |
| Union  | `not-renderable in .md`        | `.union()` | All unique elements |
| Intersection   | `&`    | `.intersection()`         | Common elements          |                     |
| Difference     | `-`    | `.difference()`           | Elements only in one set |                     |
| Symmetric Diff | `^`    | `.symmetric_difference()` | In either but not both   |                     |
| Subset         | ⬇      | `.issubset()`             | Check subset relation    |                     |
| Superset       | ⬆      | `.issuperset()`           | Check superset relation  |                     |

---