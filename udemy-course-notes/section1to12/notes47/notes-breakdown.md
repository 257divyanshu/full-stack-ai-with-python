## ☕ Step 1: Basic decorator idea

A **decorator** is just a **function that modifies another function** — without permanently changing its code.

Here:

```python
def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper
```

* `my_decorator` takes a function (`func`) as input.
* It defines another function `wrapper()` that adds extra behavior:

  * Runs code **before** and **after** `func()`.
* Finally returns `wrapper`.

So when you apply:

```python
@my_decorator
def greet():
    print("Hello from decorators class from chaicode")
```

…it’s **equivalent to**:

```python
greet = my_decorator(greet)
```

Now calling `greet()` actually calls `wrapper()` — which wraps around the original logic.

---

## ☕ Step 2: Why `@wraps(func)` matters

Without `@wraps(func)`, the metadata of your original function (like `__name__`, `__doc__`) gets replaced by the wrapper’s.

Example **without** `@wraps`:

```python
print(greet.__name__)  # outputs: wrapper
```

Example **with** `@wraps(func)`:

```python
print(greet.__name__)  # outputs: greet ✅
```

So this line:

```python
@wraps(func)
def wrapper():
```

is there to **preserve the original function’s identity** (name, docstring, annotations).

---

## ☕ Step 3: Execution flow

When you call `greet()`:

1. `wrapper()` runs (because of the decorator).
2. Prints `"Before function runs"`.
3. Executes the original `greet()` → prints `"Hello from decorators class from chaicode"`.
4. Prints `"After function runs"`.

✅ **Output:**

```
Before function runs
Hello from decorators class from chaicode
After function runs
greet
```

---

### 🧠 Summary Table

| Concept          | Description                             | Example                            |
| ---------------- | --------------------------------------- | ---------------------------------- |
| Decorator        | Function that modifies another function | `@my_decorator`                    |
| `@wraps(func)`   | Keeps original metadata                 | Keeps `__name__`, `__doc__` intact |
| Wrapper function | Adds pre/post logic                     | `print("Before...")` etc.          |