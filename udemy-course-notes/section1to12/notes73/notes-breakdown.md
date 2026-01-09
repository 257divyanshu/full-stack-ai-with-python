### 🧩 What’s happening in this code?

```python
from multiprocessing import Process
import time
```

We import the `Process` class (from the `multiprocessing` module) to create **separate processes**, not threads.

---

### Step 1: Define the CPU-heavy function

```python
def crunch_number():
    print(f"Started the count process...")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"Ended the count process...")
```

This is the same kind of **pure computation** loop as before (no I/O, just raw CPU usage).

---

### Step 2: Create and start two processes

```python
p1 = Process(target=crunch_number)
p2 = Process(target=crunch_number)

p1.start()
p2.start()
p1.join()
p2.join()
```

✅ Each `Process` runs **in its own Python interpreter**, **in a separate CPU core**, with **its own memory space**.
That’s why the **Global Interpreter Lock (GIL)** no longer applies here.

🧠 This means your two processes truly run **in parallel** if your machine has multiple cores (which most modern CPUs do).

---

### Step 3: Timing the execution

```python
start = time.time()
...
end = time.time()

print(f"Total time with multi-processing is {end - start:.2f} seconds")
```

If you compare this to the *threading* version you ran earlier:

* The **threading version** likely took ~6–8 seconds.
* This **multiprocessing version** will probably take ~3–4 seconds (roughly half), because both CPU cores are used at once.

---

### 🧠 Key takeaway

| Type              | True parallelism | Shares memory | GIL affected | Best for                                   |
| ----------------- | ---------------- | ------------- | ------------ | ------------------------------------------ |
| `threading`       | ❌ No             | ✅ Yes         | ✅ Yes        | I/O-bound tasks (waiting, network, etc.)   |
| `multiprocessing` | ✅ Yes            | ❌ No          | ❌ No         | CPU-bound tasks (computation, loops, etc.) |

---