We’re now moving to **threading and concurrency** — one of the most exciting (and sometimes tricky) areas in Python.

Before we jump into your next notes file, here’s a quick heads-up on what’s coming:

---

### 🧠 Quick Intro to Threading & Concurrency

| Concept                           | Meaning                                                                                                    |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Thread**                        | A lightweight process — it runs a part of your program **concurrently** with others.                       |
| **Concurrency**                   | Doing multiple tasks **seemingly at the same time** (e.g., brewing chai while toasting bread).             |
| **Parallelism**                   | Actually running multiple tasks **at the same instant**, using multiple CPU cores.                         |
| **GIL (Global Interpreter Lock)** | A Python mechanism that allows only one thread to execute Python code at a time — affects CPU-bound tasks. |

---

In Python, we usually use:

* `threading` → for **I/O-bound** tasks (e.g., file downloads, waiting for input)
* `multiprocessing` → for **CPU-bound** tasks (e.g., image processing, calculations)
* `asyncio` → for **asynchronous, single-threaded concurrency**

---

✅ Example (we’ll see this soon):

```python
import threading

def make_chai():
    print("Brewing chai...")

t = threading.Thread(target=make_chai)
t.start()
t.join()
```

This starts a new thread that runs `make_chai()` **while your main program continues running**.