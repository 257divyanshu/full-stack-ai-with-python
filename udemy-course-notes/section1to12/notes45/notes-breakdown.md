## 🧩 **Snippet’s Intent**

> To teach how **coroutines** work — i.e., how you can use the `send()` method with `yield` to both *receive* and *send* data inside a generator.

---

### 🧠 Code Breakdown

```python
def chai_customer():
    print("Welcome! What chai would you like?")
    order = yield
    while True:
        print(f"Preparing: {order}")
        order = yield
```

---

### 🧾 Step-by-step Explanation

1. **Function definition**

   The function has `yield` statements — so it’s a **generator**.
   But here, `yield` is used differently:

   * Instead of *producing* values,
   * It’s also used to *receive* values from the outside via `.send()`.

---

2. **Start the generator**

   ```python
   stall = chai_customer()
   next(stall)
   ```

   * When you first call `chai_customer()`, nothing runs yet.
     It just creates the generator object.
   * The first `next(stall)` runs up to the first `yield`:

     ```
     Welcome! What chai would you like?
     ```

     Now it pauses **waiting for input** — `order = yield` is waiting to receive something.

---

3. **Send in a value**

   ```python
   stall.send("Masala Chai")
   ```

   * The value `"Masala Chai"` gets assigned to `order`.
   * The generator resumes and executes:

     ```python
     print(f"Preparing: {order}")
     ```

     ✅ Output:

     ```
     Preparing: Masala Chai
     ```
   * Then it hits `order = yield` again — pauses, waiting for the next input.

4. **Send again**

   ```python
   stall.send("Lemon Chai")
   ```

   Output:

   ```
   Preparing: Lemon Chai
   ```

---

### 🧮 Final Output

```
Welcome! What chai would you like?
Preparing: Masala Chai
Preparing: Lemon Chai
```

---

### ⚙️ What’s Happening Internally

* `next(stall)` — starts the generator (runs until the first `yield`).
* `.send(value)` — resumes the generator, and the `yield` expression inside receives that value.

Essentially, **`yield` acts as both:**

* a *pause point* (like before),
* and a *communication channel* for values coming *into* the generator.

---

### 🧩 Analogy

Imagine a chai stall ☕

* The stall owner (`generator`) says, “Welcome! What chai would you like?”
* You (`send`) respond: “Masala Chai”
* He prepares it and waits for the next order.
* You send again: “Lemon Chai”
* He prepares that too — and waits again.

This loop continues until you stop the program.

---

### 🧠 Key Concept — **Coroutine**

This pattern is called a **coroutine**:
a function that can *pause and resume*, while *receiving data dynamically* each time it resumes.

---

### ⚠️ Common Pitfall

You must always **prime** the generator (run `next()` once) *before* calling `.send(value)`,
otherwise Python will raise:

```
TypeError: can't send non-None value to a just-started generator
```