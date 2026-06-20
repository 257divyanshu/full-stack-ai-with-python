### 1. Why is `messages` an array?

Because LLMs are designed to work with **conversations**, not just single prompts.

A conversation consists of multiple messages:

```python
messages = [
    {"role": "user", "content": "Hi"},
    {"role": "assistant", "content": "Hello!"},
    {"role": "user", "content": "How are you?"}
]
```

The model sees the entire conversation history and generates the next response.

So yes, **you can send multiple messages in one API call**.

---

### 2. Why do we have `role` and `content`?

Each message needs two pieces of information:

#### `content`

The actual text.

```python
{
    "content": "What is the Pythagorean theorem?"
}
```

#### `role`

Who said that text.

```python
{
    "role": "user",
    "content": "What is the Pythagorean theorem?"
}
```

Without the role, the model wouldn't know whether the text came from the user, the assistant, or the system.

---

### 3. What does `role = "user"` mean?

It means:

> "This message was written by the human user."

Example:

```python
{
    "role": "user",
    "content": "What is 2 + 2?"
}
```

The model interprets this as a user asking a question.

---

### 4. What does `role = "system"` mean?

It means:

> "These are instructions that define how the AI should behave."

Example:

```python
{
    "role": "system",
    "content": "You are a mathematics expert."
}
```

This is not part of the conversation itself.

Instead, it acts like a set of rules or guidance for the model.

---

### 5. What is System Prompting?

System prompting is the practice of giving instructions to the model through a system message.

Example:

```python
{
    "role": "system",
    "content": "You are a mathematics expert."
}
```

Now when the user asks:

```python
{
    "role": "user",
    "content": "What is the Pythagorean theorem?"
}
```

the model answers from the perspective of a math expert.

---

### 6. What is happening in your first code snippet?

```python
messages=[
    {
        "role": "user",
        "content": "Hello there Gemini! Briefly state the Pythagoras theorem with its formula."
    }
]
```

Conversation:

```text
User:
"Hello there Gemini! Briefly state the Pythagoras theorem with its formula."
```

No special instructions are given.

The model answers using its default behavior.

---

### 7. What is happening in your second code snippet?

```python
messages=[
    {
        "role": "system",
        "content": "You are an expert in Mathematics and you are supposed to answer only and only math related questions."
    },
    {
        "role": "user",
        "content": "Hello there Gemini! Briefly state the Pythagoras theorem with its formula."
    }
]
```

Conversation:

```text
System:
"You are an expert in Mathematics and answer only math questions."

User:
"Briefly state the Pythagoras theorem with its formula."
```

Now the model first reads the system instruction, then the user question, and generates a response accordingly.

---

### Mental Model

Think of the `messages` array as a chat transcript:

```text
[
    System : "You are a math teacher."
    User   : "What is Pythagoras theorem?"
]
```

The model reads the entire transcript from top to bottom and then produces the next assistant message.

In practice, most AI applications send something like:

```python
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "What is Python?"},
    {"role": "assistant", "content": "Python is a programming language."},
    {"role": "user", "content": "Who created it?"}
]
```

The model sees the whole conversation and answers:

```text
Guido van Rossum created Python.
```

This ability to send conversation history is the main reason `messages` is an array instead of a single string.
