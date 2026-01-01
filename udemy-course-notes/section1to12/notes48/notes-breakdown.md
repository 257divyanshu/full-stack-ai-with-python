## ☕ Step 1: Decorator with flexible arguments

Here’s the decorator:

```python
def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"🚀 Calling: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"✅ Finished: {func.__name__}")
        return result
    return wrapper
```

🧩 Explanation:

* `log_activity` takes a function `func` (the one being decorated).
* The inner `wrapper()` function:

  * Accepts **any arguments** with `*args` and `**kwargs`.
  * Prints a log **before** and **after** calling the actual function.
  * Calls the real function `func(*args, **kwargs)` and stores the result.
  * Returns the result to preserve normal behavior.

---

## ☕ Step 2: Decorating the target function

```python
@log_activity
def brew_chai(type, milk="no"):
    print(f"Brewing {type} chai and milk status {milk}")
```

is equivalent to:

```python
brew_chai = log_activity(brew_chai)
```

Now, every time you call `brew_chai()`, you’re really calling the **wrapper** that adds logging behavior.

---

## ☕ Step 3: Execution flow

When you run:

```python
brew_chai("Masala")
```

The following happens:

1. `wrapper()` runs.
2. Prints `🚀 Calling: brew_chai`.
3. Executes the real `brew_chai("Masala")`, printing
   → `Brewing Masala chai and milk status no`
4. Prints `✅ Finished: brew_chai`.

✅ **Output:**

```
🚀 Calling: brew_chai
Brewing Masala chai and milk status no
✅ Finished: brew_chai
```

---

## 🧠 Why this pattern matters

| Concept           | Description                                                                  |
| ----------------- | ---------------------------------------------------------------------------- |
| `@wraps(func)`    | Keeps metadata (name, docstring, etc.)                                       |
| `*args, **kwargs` | Makes decorator compatible with *any* function signature                     |
| Logging Decorator | Helps monitor when functions start/finish (useful in debugging or analytics) |