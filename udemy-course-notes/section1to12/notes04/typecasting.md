## 🧩 What is Typecasting?

**Typecasting** (or **type conversion**) means **changing the data type** of a value into another type — for example, from a string to an integer, or from an integer to a float.

In Python:

> You can explicitly convert (cast) one data type into another using *built-in functions* like `int()`, `float()`, `str()`, etc.

---

## ⚙️ Why Typecasting is Needed

Python is a **strongly typed language**, meaning:

* It doesn’t automatically convert types for operations.
* You can’t add an integer and a string directly, for example.

### ❌ This causes an error:

```python
age = 25
msg = "I am " + age + " years old"
```

```
TypeError: can only concatenate str (not "int") to str
```

### ✅ But this works:

```python
msg = "I am " + str(age) + " years old"
```

That’s **typecasting** — you converted an integer (`age`) to a string.

---

## 🧠 Types of Typecasting

Python supports **two** kinds of typecasting:

| Type         | Meaning                       | Example             |
| ------------ | ----------------------------- | ------------------- |
| **Implicit** | Automatically done by Python  | `a = 5 + 3.0 → 8.0` |
| **Explicit** | Manually done using functions | `int("5") → 5`      |

---

## 🔹 1. Implicit Typecasting (Automatic)

Python automatically promotes one data type to another when needed — *without loss of information*.

### Example:

```python
a = 5      # int
b = 2.5    # float

result = a + b
print(result)      # 7.5
print(type(result))  # <class 'float'>
```

💡 Here, Python automatically converted `a` (int) into a float before addition.

---

## 🔹 2. Explicit Typecasting (Manual)

You can manually convert data types using built-in constructors:

| Function  | Converts to    | Example                      | Output             |
| --------- | -------------- | ---------------------------- | ------------------ |
| `int()`   | Integer        | `int(3.8)`                   | `3`                |
| `float()` | Floating point | `float(5)`                   | `5.0`              |
| `str()`   | String         | `str(25)`                    | `"25"`             |
| `bool()`  | Boolean        | `bool(0)`                    | `False`            |
| `list()`  | List           | `list("abc")`                | `['a', 'b', 'c']`  |
| `tuple()` | Tuple          | `tuple([1,2])`               | `(1, 2)`           |
| `set()`   | Set            | `set([1,2,2])`               | `{1, 2}`           |
| `dict()`  | Dictionary     | `dict([(1, "a"), (2, "b")])` | `{1: 'a', 2: 'b'}` |

---

## 🧪 Examples

### 🧮 String → Integer

```python
num_str = "100"
num_int = int(num_str)
print(num_int + 20)  # 120
```

### 💬 Integer → String

```python
age = 21
text = "I am " + str(age) + " years old."
print(text)
```

### 🔢 Float → Integer

```python
value = 9.99
print(int(value))  # 9  (decimal part removed)
```

### ✅ Integer → Float

```python
print(float(10))  # 10.0
```

### 🔁 List → Set (removes duplicates)

```python
nums = [1, 2, 2, 3]
unique_nums = set(nums)
print(unique_nums)  # {1, 2, 3}
```

---

## ⚠️ Common Pitfalls

### ❌ Invalid conversions

```python
int("hello")   # ValueError
float("abc")   # ValueError
```

Only strings that represent *valid numbers* can be converted:

```python
int("100")   # ✅ Works
float("3.14")  # ✅ Works
```

---

## ✅ Summary

| Conversion Type | Description                                | Example                |
| --------------- | ------------------------------------------ | ---------------------- |
| **Implicit**    | Python auto-converts smaller → larger type | `3 + 2.5 → 5.5`        |
| **Explicit**    | You manually convert using type functions  | `str(5) → '5'`         |
| **Common Uses** | String ↔ Number, List ↔ Set/Tuple          | `set([1,2,2]) → {1,2}` |

---