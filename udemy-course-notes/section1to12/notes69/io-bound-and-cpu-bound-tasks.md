### 1. I/O-Bound Tasks

**Definition:** These tasks spend most of their time **waiting**. The CPU is sitting idle, waiting for data to come from somewhere else (a hard drive, a network, a database, etc.).

Because the CPU is mostly idle, Python's `threading` (or `asyncio`) works well here. While one thread waits for data, the CPU can switch to another thread to send a different request.

**Common Examples:**

* **Network Requests (Web Scraping/APIs):** Sending a request to a website and waiting for the server to respond. The speed depends on the internet connection and the remote server, not your CPU.
* **Database Queries:** Sending a SQL query to a database and waiting for the results to be returned.
* **File Operations:** Reading or writing huge files to the hard disk. The speed is limited by the disk's read/write speed.
* **User Input:** Waiting for a user to type something on the keyboard or click a button.
* **Sending Emails:** Waiting for the SMTP server to accept and deliver the message.
* **Microservice Communication:** Waiting for a response from another internal service in a distributed system.

> **Key Characteristic:** If you upgraded your processor to a faster one, these tasks would **not** get significantly faster.

---

### 2. CPU-Bound Tasks

**Definition:** These tasks spend most of their time **calculating**. The CPU is running at 100% load, crunching numbers or logic.

Because the CPU is already working as hard as it can, adding threads (which share the same CPU core in Python due to the Global Interpreter Lock) doesn't help. You need `multiprocessing` to use *multiple* CPU cores simultaneously.

**Common Examples:**

* **Image/Video Processing:** Resizing images, applying filters (like blurring or sharpening), or converting video formats (transcoding).
* **Machine Learning:** Training models, matrix multiplications, or running complex algorithms on datasets.
* **Encryption/Decryption:** Hashing passwords (e.g., SHA-256, bcrypt) or encrypting large distinct chunks of data.
* **Complex Math:** Calculating digits of Pi, finding prime numbers, or heavy financial simulations (Monte Carlo simulations).
* **Data Compression:** Zipping or unzipping large files (algorithms like GZIP or LZMA require heavy computation).
* **Search Algorithms:** Running complex search or sorting algorithms on massive lists in memory.

> **Key Characteristic:** If you upgraded your processor to a faster one, these tasks **would** finish much faster.

---

### Summary Comparison

| Feature | I/O-Bound | CPU-Bound |
| --- | --- | --- |
| **Bottleneck** | Network, Disk, Database | Processor Speed |
| **CPU State** | Mostly Idle (Waiting) | Mostly Busy (100% Usage) |
| **Python Solution** | `threading` or `asyncio` | `multiprocessing` |
| **Analogy** | Waiting for a pizza delivery. | Cooking the pizza yourself. |