This example introduces one of the **most important concurrency concepts** in Python:
🧩 **thread synchronization using Locks**.

Let’s unpack it clearly 👇

---

### 🧠 The problem

When multiple threads access and modify **shared data** (like `counter` here), you get a **race condition** — meaning:

* Two or more threads might read and write to `counter` **at the same time**.
* This can cause **unpredictable and incorrect results**, because `counter += 1` is *not atomic* (it happens in multiple CPU steps — read, increment, write).

So without control, `counter` might end up **less than expected**.

---

### 💡 The solution: `threading.Lock()`

```python
lock = threading.Lock()
```

A **Lock** ensures that only one thread can access a specific section of code at a time.

---

### 🔒 Using the lock safely

```python
with lock:
    counter += 1
```

This means:

* Acquire the lock before modifying `counter`.
* Automatically release it when the `with` block exits.

So only **one thread at a time** can execute that increment section.

---

### 🔁 Full flow

```python
threads = [threading.Thread(target=increament) for _ in range(10)]
[t.start() for t in threads]
[t.join() for t in threads]
```

You’re:

* Creating 10 threads.
* Each one increments the counter **100,000 times** safely under the lock.
* After joining all, you print the result.

---

### ✅ Final result

```
Final counter: 1000000
```

That’s correct because:
10 threads × 100,000 increments = 1,000,000 total.

Without the lock, you’d likely see a much smaller (and inconsistent) number.

---

### ⚙️ In summary

| Concept            | Meaning                                                                       |
| ------------------ | ----------------------------------------------------------------------------- |
| **Race Condition** | When threads modify shared data simultaneously, causing inconsistent results  |
| **Lock**           | A synchronization tool that ensures one thread at a time accesses shared data |
| **with lock:**     | Automatically acquires/releases the lock safely                               |
| **Use case**       | Protecting shared resources in multi-threaded environments                    |