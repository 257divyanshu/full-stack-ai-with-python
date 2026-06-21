A beginner-friendly way to think about **zero-shot prompting** is:

> You ask the model to do something without showing it any examples of the expected input-output format.

Example:

```text
Translate "Hello" to Hindi.
```

The model already knows how translation works from its training, so no example is needed.

---

### Why is it called "zero-shot"?

Because the model gets **zero examples** ("shots") before being asked to perform the task.

```text
Examples provided = 0
```

Hence:

```text
Zero-shot Prompting
```

---

### When does it work well?

When the task is:

* Simple
* Common
* Well represented in the model's training data

Examples:

```text
Summarize this paragraph.
```

```text
Translate this sentence.
```

```text
What is the capital of France?
```

```text
Explain recursion in simple terms.
```

---

### Limitation

Sometimes the model doesn't understand the exact format you want.

For example:

```text
Classify this review as Positive or Negative.
Review: "The movie was okay."
```

The model may return:

```text
The sentiment appears to be neutral.
```

instead of strictly:

```text
Positive
```

or

```text
Negative
```

In such cases, developers often move to **few-shot prompting**, where they provide a couple of examples first.

---

### Practical takeaway

Zero-shot prompting is usually the **first thing you try** because it's the simplest:

```text
Just tell the model what you want.
```

If the responses are inconsistent or not in the desired format, then you start adding examples (few-shot prompting) or stronger instructions (system prompting).
