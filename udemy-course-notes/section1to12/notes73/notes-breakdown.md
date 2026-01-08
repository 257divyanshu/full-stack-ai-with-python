### 🧩 Code walkthrough

```python
import threading
import time
```

→ We import the `threading` module to create threads, and `time` to measure how long the work takes.

---

### Step 1: Define the task (the worker function)

```python
def brew_chai():
    print(f"{threading.current_thread().name} started brewing...")
    count = 0
    for _ in range(100_000_000):  # do a lot of CPU work
        count += 1
    print(f"{threading.current_thread().name} finished brewing...")
```

✅ This function simulates *CPU-heavy* work — no waiting or sleeping, just pure computation.
We’re also printing which thread is working (using `threading.current_thread().name`).

---

### Step 2: Create two threads

```python
thread1 = threading.Thread(target=brew_chai, name="Barista-1")
thread2 = threading.Thread(target=brew_chai, name="Barista-2")
```

→ Each thread is assigned the same task (`brew_chai`), but they’ll run independently.

---

### Step 3: Measure execution time

```python
start = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end = time.time()
```

* `.start()` begins execution of each thread concurrently.
* `.join()` waits for both to finish before moving forward.
* Then we calculate the total time.

---

### 🧠 Here’s the **important concept**:

Even though we’re using **two threads**, this code **will not run twice as fast** on most Python interpreters (especially CPython).

Why?

---

### 🔒 The Global Interpreter Lock (GIL)

Python’s **GIL** allows only **one thread to execute Python bytecode at a time**, even on multi-core CPUs.

So for **CPU-bound** tasks like this (heavy computation, loops, math, etc.):

* Threads do **not** actually run in true parallel.
* They *take turns* running on the CPU.
* Therefore, total runtime ≈ same as doing it in a single thread.

✅ Threads are useful for **I/O-bound** tasks — like waiting for network responses, reading files, etc.
❌ But not for **CPU-bound** ones like this — here, you’d use `multiprocessing` instead.

---

### 🧪 Try this yourself:

Compare:

```python
# Using threads
threading.Thread(...)
```

vs

```python
# Using processes
from multiprocessing import Process
Process(target=brew_chai)
```

You’ll notice `multiprocessing` actually runs both in *parallel* (and likely finishes faster).

---

### 🕐 Example output (approximate)

```
Barista-1 started brewing...
Barista-2 started brewing...
Barista-1 finished brewing...
Barista-2 finished brewing...
total time taken: 6.83 seconds
```

(If you ran it sequentially, you might see ~6.5 seconds too — proving threads didn’t help.)