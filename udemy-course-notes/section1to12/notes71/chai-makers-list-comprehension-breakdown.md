### 🧩 First, what this code does

```python
chai_makers = [
    Process(target=brew_chai, args=(f"Chai Maker #{i+1}", ))
    for i in range(3)
]
```

This creates a **list** containing 3 `Process` objects:

```python
[
 Process(target=brew_chai, args=('Chai Maker #1',)),
 Process(target=brew_chai, args=('Chai Maker #2',)),
 Process(target=brew_chai, args=('Chai Maker #3',))
]
```

So `chai_makers` becomes a list of 3 processes ready to start.

---

### 🧠 Now — Why does it “look backwards”?

That’s because **list comprehensions** in Python are written as a kind of shorthand.
They *look* like this:

```python
[new_thing for item in iterable]
```

But internally, it behaves the same as this longer form:

```python
new_list = []
for item in iterable:
    new_list.append(new_thing)
```

So your code:

```python
chai_makers = [
    Process(target=brew_chai, args=(f"Chai Maker #{i+1}", ))
    for i in range(3)
]
```

is actually equivalent to:

```python
chai_makers = []
for i in range(3):
    p = Process(target=brew_chai, args=(f"Chai Maker #{i+1}", ))
    chai_makers.append(p)
```

✅ Same meaning — different (shorter) syntax.

---

### 📖 Why Python puts `Process(...)` first

Think of list comprehensions as saying:

> “Make me a list **of this thing** for each item in that range.”

So the part **before `for`** describes *what to build*,
and the part **after `for`** describes *where to get values from*.

It’s almost like reading in English:

> “Create a list of `Process(...)` for each `i` in `range(3)`.”

---

### ⚙️ Quick mental model

| Regular loop form                          | List comprehension form               |
| ------------------------------------------ | ------------------------------------- |
| `for i in range(3):` <br> `→ do something` | `[do something for i in range(3)]`    |
| Emphasizes the loop first                  | Emphasizes the *resulting list* first |

---

### ✅ Key takeaway

You’re right — in *normal loops*, `for` comes first.
But **list comprehensions flip it** because they’re focused on *creating a new list*, not just looping.

That’s why the “action” (`Process(...)`) comes before the `for`.