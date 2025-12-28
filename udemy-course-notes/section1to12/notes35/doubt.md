## 1️⃣ What "default arguments" are

When you define a function in Python, you can **give a parameter a default value**:

```python
def greet(name="Guest"):
    print(f"Hello {name}!")
```

* If you call `greet()` without passing a value, Python uses `"Guest"` as the **default argument**.
* If you pass a value, that value overrides the default.

✅ Example:

```python
greet()          # Hello Guest!
greet("Aman")    # Hello Aman!
```

---

## 2️⃣ Mutable vs Immutable

* **Immutable objects**: integers, strings, tuples → cannot be changed after creation
* **Mutable objects**: lists, dictionaries, sets → can be changed

Example:

```python
x = [1, 2, 3]   # list → mutable
x.append(4)     # list is changed → [1, 2, 3, 4]

y = "hello"     # string → immutable
y.replace("h", "H")  # creates a new string, original y is unchanged
```

---

## 3️⃣ Default mutable arguments

If you write:

```python
def chai_order(order=[]):  # <- default value is a list (mutable)
    order.append("Masala")
    print(order)
```

* The `[]` **is created once when the function is defined**, not each time it’s called.
* That means **all future calls** to `chai_order()` will use the **same list** unless you pass a new one.
* This is why it “persists across calls.”

---

### 🔍 Example of the problem

```python
def chai_order(order=[]):
    order.append("Masala")
    print(order)

chai_order()   # prints ['Masala']
chai_order()   # prints ['Masala', 'Masala']
chai_order()   # prints ['Masala', 'Masala', 'Masala']
```

* The list keeps growing because it **remembers the previous modifications**.
* This is usually **not what you want**.

---

## 4️⃣ The safe way

```python
def chai_order(order=None):
    if order is None:
        order = []  # create a fresh list each time
    order.append("Masala")
    print(order)
```

* `None` is immutable → safe to use as a default.
* Inside the function, you create a **new list** for each call.
* Now each call is independent:

```python
chai_order()  # ['Masala']
chai_order()  # ['Masala']
```

✅ Works as expected.

---

### 🔑 Summary

* **Default arguments** → values assigned to parameters if the caller doesn’t pass one.
* **Mutable default arguments** → lists, dicts, sets → only created once → can be modified by future calls.
* **Problem** → they “persist across calls” and keep previous changes.
* **Solution** → use `None` as default and create a fresh mutable object inside the function.