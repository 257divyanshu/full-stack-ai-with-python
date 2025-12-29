## 🧩 **Snippet’s Intent**

> To teach:
>
> 1. How to write and access **docstrings**
> 2. Accessing **function metadata** (`__name__`)
> 3. Using `help()` to see documentation
> 4. Writing detailed **parameter and return documentation**

---

## 1️⃣ Docstrings

```python
def chai_flavor(flavor="masala"):
    """Return the flavor of chai."""
    chai = "ginger"
    return flavor
```

* Triple quotes `""" ... """` immediately after the function definition → **docstring**.
* Purpose:

  * Describe **what the function does**
  * Helpful for **self-documenting code** and for others reading your code.

✅ Access docstring:

```python
print(chai_flavor.__doc__)  # Output: Return the flavor of chai.
```

---

## 2️⃣ Function Metadata

```python
print(chai_flavor.__name__)  # Output: chai_flavor
```

* `__name__` → gives the **name of the function**
* Useful when dynamically handling functions, logging, or debugging.

---

## 3️⃣ `help()` function

```python
help(len)
```

* Shows **built-in documentation** for any object (function, class, module)
* You can also use `help(chai_flavor)` for your own functions.
* Displays:

  * Docstring
  * Parameters
  * Return value
  * Source signature

---

## 4️⃣ Detailed Function Documentation

```python
def generate_bill(chai=0, samosa=0):
    """
    Calculate the total bill for chai and samosa

    :param chai: Number of chai cups (10 rupees each)
    :param samosa: Number of samosa (15 rupees each)
    :return: (total amount, thank you message as string)
    """
    total = chai*10 + samosa*15
    return total, "Thank you for visiting chaicode.com"
```

* Docstring explains:

  * **Purpose of the function**
  * **Parameters** with types and meaning
  * **Return value**
* This format is widely used in **professional Python code** (often called **reStructuredText** or **Google docstring style**)

✅ Example usage:

```python
bill, message = generate_bill(3, 2)
print(bill)      # 3*10 + 2*15 = 60
print(message)   # "Thank you for visiting chaicode.com"
```

---

### 🧠 Key Concepts Illustrated

| Concept                              | Explanation                                       |
| ------------------------------------ | ------------------------------------------------- |
| **Docstring (`"""..."""`)**          | Function documentation string                     |
| **`__doc__`**                        | Access the docstring programmatically             |
| **`__name__`**                       | Function’s name                                   |
| **`help()`**                         | Shows documentation for functions/classes/modules |
| **Parameter & return documentation** | Explains input/output clearly for users           |

---