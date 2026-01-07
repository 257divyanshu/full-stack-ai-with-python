### 🧠 Concept Recap — Multiprocessing vs Threading

| Feature                       | Threading                                                            | Multiprocessing                                                |
| ----------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------- |
| Runs                          | Multiple **threads** in one process                                  | Multiple **independent processes**                             |
| Memory                        | Shared memory space                                                  | Separate memory space for each process                         |
| GIL (Global Interpreter Lock) | Affected by GIL (only one thread executes Python bytecode at a time) | **Bypasses GIL** (each process has its own Python interpreter) |
| Best for                      | I/O-bound tasks (like file, network, waiting)                        | CPU-bound tasks (like computation, image processing)           |

So — threads are lighter, but processes are more powerful for heavy computation.

---

### 🧩 Code Breakdown

```python
from multiprocessing import Process
import time
```

* `Process` from `multiprocessing` lets you create *true parallel* processes.
* `time.sleep()` is used to simulate work (like brewing).

---

```python
def brew_chai(name):
    print(f"Start of {name} chai brewing")
    time.sleep(3)
    print(f"End of {name} chai brewing")
```

Each process will run this function — each one will act like an independent chai maker ⛾.

---

```python
if __name__ == "__main__":
```

This guard is **required** for multiprocessing on Windows (and recommended always).
Without it, each child process would try to re-import and re-run the entire file — leading to infinite process spawning.

---

```python
chai_makers = [
    Process(target=brew_chai, args=(f"Chai Maker #{i+1}", ))
    for i in range(3)
]
```

* You’re creating **3 Process objects**.
* Each process will execute `brew_chai("Chai Maker #1")`, `brew_chai("Chai Maker #2")`, and so on.

---

```python
for p in chai_makers:
    p.start()
```

All 3 processes are started **concurrently** — and since they’re in separate memory spaces, they can truly run in parallel on multiple CPU cores. 🧠⚙️

---

```python
for p in chai_makers:
    p.join()
```

The `join()` ensures that the main process waits for all child processes to complete before continuing.

---

```python
print("All chai served")
```

✅ Runs only when all the child processes have finished.

---

### 🕒 Output Example (order may vary!)

Because processes run independently, their output might interleave like this:

```
Start of Chai Maker #1 chai brewing
Start of Chai Maker #2 chai brewing
Start of Chai Maker #3 chai brewing
End of Chai Maker #2 chai brewing
End of Chai Maker #1 chai brewing
End of Chai Maker #3 chai brewing
All chai served
```

(Notice how the order of finishing is *not predictable* — each process works on its own CPU core.)