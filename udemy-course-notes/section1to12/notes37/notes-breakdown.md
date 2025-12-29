## 🧩 **Snippet’s Intent**

> To teach:
>
> 1. The difference between **pure and impure functions**
> 2. **Recursion** — functions calling themselves
> 3. Using **lambda functions** with `filter` for list processing

---

## 1️⃣ Pure vs Impure Functions

```python
def pure_chai(cups):
    return cups * 10
```

* **Pure function**:

  * Output depends **only on input**
  * Does **not modify external variables**
  * Example: `pure_chai(3)` → always returns `30`

```python
total_chai = 0

def impure_chai(cups):
    global total_chai
    total_chai += cups
```

* **Impure function**:

  * Modifies a **global variable** (`total_chai`)
  * Output depends on both input and external state
  * Side effects → harder to debug, test, or reuse

✅ Concept: **Prefer pure functions when possible**.

---

## 2️⃣ Recursion

```python
def pour_chai(n):
    print(n)
    if n == 0:
        return "All cups poured"
    return pour_chai(n-1)

print(pour_chai(3))
```

* Function calls itself with a smaller number (`n-1`) until **base case** (`n==0`) is reached.
* Base case prevents infinite recursion.
* Recursive calls **return values** back up the chain.

✅ Output:

```
3
2
1
0
All cups poured
```

**Key idea:** recursion is a loop-like mechanism **implemented with function calls**.

---

## 3️⃣ Lambda Functions and `filter`

```python
chai_types = ["light", "kadak", "ginger", "kadak"]

strong_chai = list(filter(lambda chai: chai != "kadak", chai_types))
print(strong_chai)
```

* **Lambda function** → anonymous function for short operations

  ```python
  lambda chai: chai != "kadak"
  ```

  returns `True` if chai is not `"kadak"`.
* `filter()` → keeps elements where lambda returns `True`.
* `list()` → converts the filtered result back to a list.

✅ Output:

```
['light', 'ginger']
```

**Key idea:** Useful for **quick, inline filtering or transformations**.

---

### 🧠 Key Concepts Illustrated

| Concept             | Explanation                                            |
| ------------------- | ------------------------------------------------------ |
| **Pure function**   | Depends only on input, no side effects                 |
| **Impure function** | Modifies external state (global variables)             |
| **Recursion**       | Function calls itself until a base condition           |
| **Lambda function** | Anonymous, inline function for short expressions       |
| **filter()**        | Selects elements from an iterable based on a condition |