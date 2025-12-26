## 🧩 **Snippet’s Intent**

> To demonstrate how to **skip** certain iterations (`continue`) and how to **stop a loop early** (`break`).

---

## 🔹 1️⃣ The setup

```python
flavours = ["Ginger", "Out of Stock", "Lemon", "Discontinued", "Tulsi"]
```

A list of chai flavours — some are not available.

---

## 🔹 2️⃣ The loop

```python
for flavour in flavours:
    if flavour == "Out of Stock":
        continue
    if flavour == "Discontinued":
        print(f"{flavour} item found")
        break
    print(f"{flavour} item found")

print("Out side of loop")
```

Let’s go step-by-step 👇

1. Loop starts going through each flavour in order.
2. If the flavour is `"Out of Stock"`, it **skips the rest of the loop body** for that item (`continue`).
3. If the flavour is `"Discontinued"`, it prints that message and then **stops the loop completely** (`break`).
4. Otherwise, it prints that the flavour was found.
5. After the loop finishes (either by finishing all items or by `break`), it prints `"Out side of loop"`.

---

## 🔹 3️⃣ What happens when it runs

Step-by-step:

| Iteration | `flavour` value  | What happens                             |
| --------- | ---------------- | ---------------------------------------- |
| 1         | `"Ginger"`       | prints `Ginger item found`               |
| 2         | `"Out of Stock"` | `continue` → skips printing              |
| 3         | `"Lemon"`        | prints `Lemon item found`                |
| 4         | `"Discontinued"` | prints it, then `break` → stops the loop |
| 5         | `"Tulsi"`        | ❌ never reached (loop already broken)    |

✅ **Output:**

```
Ginger item found
Lemon item found
Discontinued item found
Out side of loop
```

---

## 🔹 4️⃣ Concepts Taught

| Keyword           | Meaning                                                           |
| ----------------- | ----------------------------------------------------------------- |
| `continue`        | Skips the rest of the current iteration and moves to the next one |
| `break`           | Immediately stops the loop entirely                               |
| Loop flow control | Lets you **fine-tune** when to skip or stop during iteration      |
| Post-loop code    | Code outside the loop runs only after the loop ends               |

---

## 🔹 5️⃣ Tip

You can visualize `continue` and `break` like this:

| Flow       | Effect                       |
| ---------- | ---------------------------- |
| `continue` | "Skip this one, go to next!" |
| `break`    | "Stop! Exit the loop now!"   |

---

This example completes your **loop control** lessons — together with `for`, `while`, `enumerate`, and `zip`, you now have all the essential loop patterns in Python.