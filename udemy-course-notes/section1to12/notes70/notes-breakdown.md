### 🧠 Concept Recap — What’s Happening Here?

You have **two tasks** :

1. Taking chai orders (`take_orders`)
2. Brewing chai (`brew_chai`)

If you ran them one after another **without threading**, you’d:

* take all orders first → total 3×2 = 6 seconds
* then brew chai → total 3×3 = 9 seconds
  💡 Total = **15 seconds sequentially**

But with **threads**, both run *concurrently* — while one function sleeps (e.g., waiting for I/O), the other can execute.
So total runtime ≈ **9 seconds**, not 15.

---

### 🧩 Step-by-step Breakdown

```python
import threading
import time
```

* `threading` → Python’s module to create and manage threads.
* `time.sleep()` → simulates a delay (e.g., real-world waiting).

---

```python
def take_orders():
    for i in range(1, 4):
        print(f"Taking order for #{i}")
        time.sleep(2)
```

This simulates the waiter taking 3 orders, each taking 2 seconds.

---

```python
def brew_chai():
    for i in range(1, 4):
        print(f"Brewing chai for #{i}")
        time.sleep(3)
```

This simulates brewing each chai — slower (3 seconds each).

---

```python
order_thread = threading.Thread(target=take_orders)
brew_thread = threading.Thread(target=brew_chai)
```

Here, you **create** two `Thread` objects — but they don’t start yet.
You just tell Python *what* each thread should run (`target`).

---

```python
order_thread.start()
brew_thread.start()
```

Now both threads **begin running in parallel**.
Python switches between them — while one is waiting (sleeping), the other works.

---

```python
order_thread.join()
brew_thread.join()
```

`.join()` tells the main program: “Wait here until this thread finishes.”
So the program won’t print the final message until both tasks are done.

---

```python
print(f"All orders taken and chai brewed")
```

✅ Executes only after both threads complete.

---

### 🕒 Visualization

```
Time → 

Taking order #1      (2s)
Brewing chai #1       (3s)
Taking order #2      (2s)
Brewing chai #2       (3s)
Taking order #3      (2s)
Brewing chai #3       (3s)

Both run concurrently → overlapping wait times
```