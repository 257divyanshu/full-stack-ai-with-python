Few-shot prompting is simply:

> Showing the model a few examples of the kind of response you want before asking it to perform the actual task.

---

### Zero-shot vs Few-shot

#### Zero-shot

You directly ask:

```text
Convert the following movie review into a sentiment:

Review: The movie was fantastic.
```

The model figures things out on its own.

---

#### Few-shot

You first provide examples:

```text
Review: I loved the movie.
Sentiment: Positive

Review: The movie was terrible.
Sentiment: Negative

Review: The movie was fantastic.
Sentiment:
```

Now the model sees the pattern and continues it.

Output:

```text
Positive
```

---

### Why does it work better?

The examples act like demonstrations.

Instead of merely telling the model:

```text
Classify reviews as Positive or Negative.
```

you show it:

```text
This is how I want you to do it.
```

Models generally learn patterns from examples more reliably than from instructions alone.

---

### What is the model actually learning from the examples?

Things like:

* Output format
* Tone
* Structure
* Level of detail
* Classification rules

For example:

```text
Input: 2 + 2
Output: 4

Input: 5 + 7
Output: 12

Input: 10 + 15
Output:
```

The model recognizes the pattern and continues it.

---

### Common Real-World Use Cases

#### 1. Output Formatting

```text
Question: What is Python?
Answer: Programming Language

Question: What is MongoDB?
Answer: Database

Question: What is Redis?
Answer:
```

The model learns the desired format.

---

#### 2. Classification

```text
Text: I love this product.
Label: Positive

Text: This product is awful.
Label: Negative

Text: This product is okay.
Label:
```

---

#### 3. Data Extraction

```text
Text: John is 25 years old.
Name: John
Age: 25

Text: Sarah is 30 years old.
Name: Sarah
Age: 30

Text: Mike is 40 years old.
```

The model learns the extraction pattern.

---

### Limitation

Few-shot prompting is not magic.

If your examples are:

* Incorrect
* Inconsistent
* Too few
* Poorly chosen

the model may learn the wrong pattern.

---

### Practical takeaway

A good mental model is:

```text
Zero-shot = Tell the model what to do.

Few-shot = Show the model how to do it.
```

That's why few-shot prompting is one of the most widely used prompting techniques in production AI applications.
