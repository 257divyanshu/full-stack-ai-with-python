## 🧩 **Snippet’s Intent**

> To teach the difference between a **normal function that returns a list** and a **generator function that yields values one at a time** using the `yield` keyword.

---

### 🧠 Code Breakdown

```python
def serve_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 3: Elaichi Chai"

stall = serve_chai()
```

This defines a **generator function** — any function containing `yield` becomes one.

When you call it:

```python
stall = serve_chai()
```

it **does not run the code immediately** — instead, it returns a **generator object** that can be iterated over.

If you run:

```python
for cup in stall:
    print(cup)
```

you’ll get:

```
Cup 1: Masala Chai
Cup 2: Ginger Chai
Cup 3: Elaichi Chai
```

---

### ⚙️ The Difference Between `return` and `yield`

| Feature     | `return`                        | `yield`                        |
| ----------- | ------------------------------- | ------------------------------ |
| Execution   | Ends the function immediately   | Pauses and remembers the state |
| Memory use  | Must hold all data at once      | Produces one item at a time    |
| Reusability | Function must restart each time | Continues from last pause      |
| Example use | `get_chai_list()`               | `get_chai_gen()`               |

---

### 🧾 Example Comparison

```python
def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]

def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"
```

**Normal Function:**

```python
print(get_chai_list())
# Output: ['Cup 1', 'Cup 2', 'Cup 3']
```

**Generator Function:**

```python
chai = get_chai_gen()
print(next(chai))  # Cup 1
print(next(chai))  # Cup 2
print(next(chai))  # Cup 3
print(next(chai))  # ❌ StopIteration (no more cups)
```

---

### 🧠 Key Concept — The `next()` Function

`next()` is how you **manually fetch** the next value from a generator.
Each time it resumes execution from where it last paused (after the previous `yield`).

When all yields are done → Python raises `StopIteration`, signaling the generator is exhausted.

---


### ✅ Quick Summary

* `yield` makes a function a generator.
* Generators **save memory** — values are produced one by one.
* Use `next()` to fetch manually, or a `for` loop to consume automatically.
* When all values are done, `StopIteration` occurs.