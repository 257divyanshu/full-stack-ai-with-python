## 🧩 **Snippet’s Intent**

> To teach how to **iterate over multiple sequences together** using `zip()`.

---

## 🔹 1️⃣ Using `zip()` in a loop

```python
names = ["Hitesh", "Meera", "Sam", "Ali"]
bills = [50, 70, 100, 55]

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")
```

✅ **Explanation:**

* `zip(names, bills)` pairs elements from both lists together:

  * First pair: `("Hitesh", 50)`
  * Second pair: `("Meera", 70)`
  * … and so on.
* `for name, amount in zip(...)` **unpacks each pair** into two variables.
* Then the loop prints each name with their corresponding bill.

---

## 🔹 2️⃣ Example Output

```
Hitesh paid 50 rupees
Meera paid 70 rupees
Sam paid 100 rupees
Ali paid 55 rupees
```

---

## 🔹 3️⃣ Concepts Taught

| Concept            | Explanation                                                       |
| ------------------ | ----------------------------------------------------------------- |
| `zip()`            | Combines two or more sequences into pairs                         |
| Loop unpacking     | `for name, amount in zip(...)` separates each pair into variables |
| Parallel iteration | Processes multiple lists **together**                             |
| f-strings          | Combines variables into formatted output                          |

---

## 🔹 4️⃣ Tip

* If lists have **different lengths**, `zip()` stops at the **shortest** list.
* You can also use `zip_longest` from `itertools` to handle unequal lengths.

Example with `zip_longest`:

```python
from itertools import zip_longest

names = ["Hitesh", "Meera", "Sam", "Ali"]
bills = [50, 70, 100]

for name, amount in zip_longest(names, bills, fillvalue=0):
    print(f"{name} paid {amount} rupees")
```

✅ Output:

```
Hitesh paid 50 rupees
Meera paid 70 rupees
Sam paid 100 rupees
Ali paid 0 rupees
```

---

This nicely complements your **for loop summary**, showing how to handle **parallel iteration over multiple sequences**.