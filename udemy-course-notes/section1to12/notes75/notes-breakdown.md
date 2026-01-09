This code is another **threading example** — this time showing how to pass **arguments** into a thread function and how multiple tasks overlap in time.

Let’s break it down clearly 👇

---

### 🧠 What’s happening

You define a function:

```python
def prepare_chai(type_, wait_time):
    print(f"{type_} chai: brewing...")
    time.sleep(wait_time)
    print(f"{type_} chai: Ready.")
```

Each chai type takes a different time to “brew” (using `time.sleep()`).

---

### ⚙️ Creating threads with arguments

```python
t1 = threading.Thread(target=prepare_chai, args=("Masala", 2))
t2 = threading.Thread(target=prepare_chai, args=("Ginger", 3))
```

* `target` → which function to run in the thread
* `args` → tuple of arguments to pass to that function

  * so `t1` runs `prepare_chai("Masala", 2)`
  * `t2` runs `prepare_chai("Ginger", 3)`

---

### 🧵 Starting and joining threads

```python
t1.start()
t2.start()
t1.join()
t2.join()
```

* `.start()` launches both tasks **at the same time**
* `.join()` waits for both threads to complete before moving on

---

### 🕒 Expected output timing

Approximate output order:

```
Masala chai: brewing...
Ginger chai: brewing...
Masala chai: Ready.
Ginger chai: Ready.
```

⏱ Total time taken: ~3 seconds
(because both chai types brew *concurrently*)

If you ran them **sequentially**, it would take 2 + 3 = **5 seconds**.

---

### 🧩 Why this works

Both threads spend time in `time.sleep()` — that’s an I/O-like wait where the **GIL is released**, allowing the other thread to run.
So Python threading gives you real concurrency *for such tasks*.