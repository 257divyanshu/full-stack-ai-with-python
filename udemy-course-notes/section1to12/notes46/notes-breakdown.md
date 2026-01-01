## ☕ Part 1: `yield from`

```python
def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"

def imported_chai():
    yield "Matcha"
    yield "Oolong"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)
```

### 🔍 What’s happening:

* `full_menu()` uses `yield from` to **delegate** iteration to another generator.
* Instead of writing:

  ```python
  for chai in local_chai():
      yield chai
  ```

  You can just say:

  ```python
  yield from local_chai()
  ```

  It’s cleaner and automatically forwards all values.

✅ **Output:**

```
Masala Chai
Ginger Chai
Matcha
Oolong
```

### 🧠 Concept

> `yield from` lets one generator “include” another generator’s output seamlessly.
> It flattens nested generators — like merging multiple chai menus into one unified menu.

---

## ☕ Part 2: `.close()` — Graceful Cleanup in Generators

```python
def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order"
    except:
        print("Stall closed, No more chai")

stall = chai_stall()
print(next(stall))
stall.close()  # cleanup
```

### 🔍 Step-by-step:

1. `stall = chai_stall()`
   → creates generator object.

2. `next(stall)`
   → starts the generator, runs until first `yield`.
   → output: `"Waiting for chai order"`

3. `stall.close()`
   → sends a **`GeneratorExit`** exception inside the generator.

4. Inside `chai_stall()`:

   ```python
   except:
       print("Stall closed, No more chai")
   ```

   catches it and prints a cleanup message.

✅ **Output:**

```
Waiting for chai order
Stall closed, No more chai
```

---

### ⚙️ Summary

| Feature      | Purpose                                 | Example                   | Behavior                          |
| ------------ | --------------------------------------- | ------------------------- | --------------------------------- |
| `yield from` | Delegate part of a generator to another | `yield from local_chai()` | Flattens multiple generators      |
| `.close()`   | Stop generator gracefully               | `stall.close()`           | Raises `GeneratorExit` internally |