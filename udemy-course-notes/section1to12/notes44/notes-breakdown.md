## 🧩 **Snippet’s Intent**

> To demonstrate how generators can produce *endless sequences* lazily — and how each generator object keeps track of its own internal state.

---

### 🧠 Code Breakdown

```python
def infinite_chai():
    count = 1
    while True:
        yield f"Refill #{count}"
        count += 1
```

---

### 🧾 Step-by-step

1. **`while True:`** → creates an *infinite loop* (will never stop unless you break it or run out of memory).

2. **`yield f"Refill #{count}"`** → sends one value at a time.

3. Each call to `next()` resumes *right where the generator left off*, remembering the value of `count`.

---

### 🧩 Creating Two Independent Generators

```python
refill = infinite_chai()
user2 = infinite_chai()
```

Each call to `infinite_chai()` creates a **separate generator object** — both have their own `count` starting at 1.

---

### 🧮 Output

First loop:

```python
for _ in range(5):
    print(next(refill))
```

✅ Output:

```
Refill #1
Refill #2
Refill #3
Refill #4
Refill #5
```

Second loop:

```python
for _ in range(6):
    print(next(user2))
```

✅ Output:

```
Refill #1
Refill #2
Refill #3
Refill #4
Refill #5
Refill #6
```

💡 Notice — `refill` and `user2` are independent:
one doesn't affect the other’s counter.

---

### ⚙️ Why This Matters

Generators like this are often used for:

* **Infinite streams** (e.g., data sensors, logs, counters).
* **Lazy sequences** (generate values on demand).
* **Simulations** (e.g., orders, refills, random events).

They’re extremely memory-efficient — they don’t store data, they *generate* it.

---