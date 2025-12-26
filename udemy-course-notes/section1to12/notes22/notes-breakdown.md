## 🧩 **Snippet’s Intent**

> To teach how to **use `while` loops** to repeat a block of code until a condition becomes `False`.

---

## 🔹 1️⃣ The `while` loop

```python
temperature = 40

while temperature < 100:
    print(f"Current temperature: {temperature}")
    # temperature = temperature + 15
    temperature += 15

print("Tea is ready to boil")
```

✅ **Explanation:**

* `while temperature < 100:` → keeps looping **as long as the condition is True**.

* Inside the loop:

  * Print the current temperature.
  * Increase `temperature` by 15 each iteration (`temperature += 15` is shorthand for `temperature = temperature + 15`).

* When `temperature >= 100`, the loop **stops**, and the program prints `"Tea is ready to boil"`.

---

## 🔹 2️⃣ Example Output

```
Current temperature: 40
Current temperature: 55
Current temperature: 70
Current temperature: 85
Current temperature: 100
Tea is ready to boil
```

*(Technically, in this code, the loop stops before printing 100 because the condition is `< 100`. If you want to include 100, adjust the condition or the loop.)*

---

## 🔹 3️⃣ Concepts Taught

| Concept             | Explanation                                              |
| ------------------- | -------------------------------------------------------- |
| `while` loop        | Repeats code **until a condition is False**              |
| Loop condition      | `temperature < 100` determines if loop continues         |
| Incrementing        | `temperature += 15` updates the variable each iteration  |
| Post-loop execution | Code **after the loop** runs once the condition is False |

---

## 🔹 4️⃣ Tip

* Always make sure the **loop condition will eventually become False**, otherwise you get an **infinite loop**.

Example of an infinite loop:

```python
temperature = 40
while temperature < 100:
    print(temperature)  # Forgot to increment temperature!
```

---

This complements your `for` loop lessons and introduces **condition-based repetition**.