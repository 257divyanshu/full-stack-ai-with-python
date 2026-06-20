The most commonly used roles are:

### 1. `system`

Provides instructions to the model.

```python
{
    "role": "system",
    "content": "You are a mathematics expert."
}
```

---

### 2. `user`

Represents a message from the human user.

```python
{
    "role": "user",
    "content": "What is the Pythagorean theorem?"
}
```

---

### 3. `assistant`

Represents a previous response from the AI.

```python
{
    "role": "assistant",
    "content": "The Pythagorean theorem states that..."
}
```

Used when maintaining conversation history.

Example:

```python
messages = [
    {"role": "user", "content": "What is Python?"},
    {"role": "assistant", "content": "Python is a programming language."},
    {"role": "user", "content": "Who created it?"}
]
```

The model can then answer:

```text
Guido van Rossum created Python.
```

because it sees the previous assistant response.

---

### 4. `tool` (or function/tool response)

Used when a tool has returned data and you want the model to use that data.

Example:

```python
{
    "role": "tool",
    "content": "Current temperature is 32°C"
}
```

You'll learn this later when working with:

* Function Calling
* Tool Calling
* AI Agents

---

### Historically

Older APIs also had:

```python
{
    "role": "function"
}
```

but modern tool-calling workflows generally use `tool`.

---