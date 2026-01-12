This is a **real-world multithreading example** 🚀

This code shows how **I/O-bound tasks** like network downloads can be sped up dramatically using threads.

---

### 🧠 Step-by-step breakdown

#### 1️⃣ Function definition

```python
def download(url):
    print(f"Starting download from {url}")
    resp = requests.get(url)
    print(f"Finished downloading from {url}, size: {len(resp.content)} bytes")
```

Each thread runs this function:

* It downloads a file from the given `url`
* Prints its size when finished

Since `requests.get()` involves **waiting for network I/O**, the CPU is mostly idle while waiting — making this a perfect case for threading.

---

#### 2️⃣ List of URLs

```python
urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
]
```

Three image endpoints from `httpbin.org`.

---

#### 3️⃣ Creating and starting threads

```python
threads = []

for url in urls:
    t = threading.Thread(target=download, args=(url,))
    t.start()
    threads.append(t)
```

Here’s the magic part 👇

* The loop creates 3 threads — one per URL.
* `.start()` launches them **almost simultaneously**.
* Each thread executes `download(url)` independently.

So while one thread is waiting for network data, others can proceed.

---

#### 4️⃣ Waiting for all threads to finish

```python
for t in threads:
    t.join()
```

* `.join()` ensures the main program waits for all downloads to complete before continuing.

---

#### 5️⃣ Measuring total time

```python
start = time.time()
...
end = time.time()
print(f"All downloads done in {end - start:.2f} seconds")
```

Without threads, total time ≈ sum of all download times.
With threads, total time ≈ longest single download time. ✅

---

### ⚡ In short

| Version    | Downloads      | Total Time           |
| ---------- | -------------- | -------------------- |
| Sequential | 3 (one by one) | ~3× longer           |
| Threaded   | 3 (parallel)   | ~same as longest one |

This is one of the **best use-cases for threading** in Python —
it doesn’t speed up CPU-heavy work, but it **greatly improves I/O-bound tasks**.