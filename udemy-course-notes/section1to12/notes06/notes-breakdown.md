### 👉 **string operations and encodings in Python**

This lesson teaches how to **work with strings** (slicing, reversing) and **handle text encodings** (Unicode → bytes and back).

---

### 🧠 Part 1: Basic string formatting (f-strings)

```python
chai_type = "Ginger chai"
customer_name = "Priya"

print(f"Order for {customer_name} : {chai_type} please !")
```

➡️ Output:

```
Order for Priya : Ginger chai please !
```

**f-strings** (formatted string literals) — a modern and simple way to embed variables directly inside strings using `{}`.

So instead of:

```python
"Order for " + customer_name + " : " + chai_type + " please!"
```

You can simply do:

```python
f"Order for {customer_name} : {chai_type} please!"
```

String interpolation is readable and efficient

---

### 🧠 Part 2: String slicing

```python
chai_description = "Aromatic and Bold"
print(f"First word: {chai_description[:8]}")
print(f"Last word: {chai_description[12:]}")
print(f"Last word: {chai_description[::-1]}")
```

| Expression               | Meaning                               | Output                |
| ------------------------ | ------------------------------------- | --------------------- |
| `chai_description[:8]`   | Take characters from start to index 7 | `"Aromatic"`          |
| `chai_description[12:]`  | Take from index 12 till end           | `"Bold"`              |
| `chai_description[::-1]` | Reverse the string                    | `"dloB dna citamorA"` |

* **String slicing** syntax: `string[start:end:step]`
* Negative step (`[::-1]`) reverses the string.
* You can extract substrings easily — useful in text processing.

---

### 🧠 Part 3: String encoding and decoding

```python
label_text = "Chai Spécial"
ecoded_label = label_text.encode("utf-8")
print(f"Non Encoded label: {label_text}")
print(f"Encoded label: {ecoded_label}")
decoded_label = ecoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")
```

Outputs something like:

```
Non Encoded label: Chai Spécial
Encoded label: b'Chai Sp\xc3\xa9cial'
Decoded label: Chai Spécial
```

#### 💡 What’s happening here:

* `.encode("utf-8")` converts a **Unicode string** → **bytes**

  * Every character is stored as one or more bytes.
  * The accented “é” becomes `\xc3\xa9` (UTF-8 encoded form).

* `.decode("utf-8")` converts **bytes** → **Unicode string** again.

---

This is an introduction to:

* **Text encodings** — how characters (especially non-English ones like “é”) are represented in bytes.
* **Why encoding matters** — for reading/writing files, networking, or APIs.

---

## 💬 In simple words:

This snippet taught us:

> “Here’s how to manipulate text in Python — extract parts, reverse it, and handle special characters safely using UTF-8 encoding.”