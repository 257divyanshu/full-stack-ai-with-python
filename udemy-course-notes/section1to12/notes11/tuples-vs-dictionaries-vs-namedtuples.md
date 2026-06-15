### 1. `tuple`

* **What**: Ordered, immutable collection
* **Access**: By index (`t[0]`)
* **Example**:

```python
t = (1, 2, 3)
print(t[0])  # 1
```

* **Pros**: Fast, memory-efficient
* **Cons**: No semantic meaning to fields

👉 Use when:

* Data is simple and position-based
* Performance matters
* Structure is fixed and obvious

---

### 2. `dict`

* **What**: Key-value mapping (mutable)
* **Access**: By key (`d["name"]`)
* **Example**:

```python
d = {"name": "A", "age": 20}
print(d["name"])  # A
```

* **Pros**: Flexible, self-descriptive
* **Cons**: Slightly slower, more memory

👉 Use when:

* Data is dynamic or may change
* Keys are not fixed
* You need frequent updates

---

### 3. `namedtuple`

* From `collections`
* **What**: Tuple with named fields (immutable)
* **Access**: By name OR index
* **Example**:

```python
from collections import namedtuple

Person = namedtuple("Person", ["name", "age"])
p = Person("A", 20)

print(p.name)  # A
print(p[0])    # A
```

* **Pros**: Readable + memory-efficient (like tuple)
* **Cons**: Still immutable, less flexible than dict

👉 Use when:

* You want **tuple performance + readable fields**
* Data structure is fixed
* You don’t need mutation

---

### 🔥 Quick Summary

| Feature     | tuple | dict     | namedtuple   |
| ----------- | ----- | -------- | ------------ |
| Mutable     | ❌     | ✅        | ❌            |
| Access      | index | key      | name + index |
| Readability | low   | high     | high         |
| Performance | high  | medium   | high         |
| Structure   | fixed | flexible | fixed        |

---

### 🧠 Rule of thumb

* **tuple** → simple, positional data
* **dict** → flexible, dynamic data
* **namedtuple** → fixed structure + readability