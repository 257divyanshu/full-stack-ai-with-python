## 🧩 **Snippet’s Intent**

> To demonstrate how to handle **multiple conditions** using logical operators (`or`) in an `if` statement, along with **input normalization**.

---

## 🔹 1️⃣ Taking and normalizing input

```python
snack = input("Enter your preferred snack: ").lower()
```

✅ **Explanation:**

* `input()` gets text from the user.
* `.lower()` ensures the input is in **lowercase**, so `"Cookies"` or `"COOKIES"` still matches `"cookies"`.

Example:

```
Enter your preferred snack: Samosa
```

→ `snack` becomes `"samosa"`

---

## 🔹 2️⃣ Conditional with `or`

```python
if snack == "cookies" or snack == "samosa":
    print(f"Great Choice! We'll serve you {snack}")
else:
    print("Sorry, we only serve cookies or samosa with tea")
```

✅ **Explanation:**

* `or` allows **either condition** to trigger the same block.
* If `snack` is `"cookies"` **or** `"samosa"` → success message
* Otherwise → rejection message

---

## 🔹 3️⃣ Example Outputs

| User Input  | Output                                          |
| ----------- | ----------------------------------------------- |
| `"cookies"` | Great Choice! We'll serve you cookies           |
| `"samosa"`  | Great Choice! We'll serve you samosa            |
| `"chips"`   | Sorry, we only serve cookies or samosa with tea |

---

## 🔹 4️⃣ Concept Being Taught

| Concept                   | Description                                              |
| ------------------------- | -------------------------------------------------------- |
| **Logical operator `or`** | Combine conditions — block runs if **any one** is `True` |
| **Input normalization**   | `.lower()` ensures consistent comparisons                |
| **Conditional flow**      | `if / else` decides which code block to run              |

---

## 🔹 5️⃣ Tip

For multiple valid options, you can also use `in` with a list (more scalable):

```python
if snack in ["cookies", "samosa"]:
    print(f"Great Choice! We'll serve you {snack}")
else:
    print("Sorry, we only serve cookies or samosa with tea")
```

This approach is cleaner when you have many acceptable options.