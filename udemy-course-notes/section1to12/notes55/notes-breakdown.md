## ☕ Code Recap

```python
class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai....")

class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardamom, ginger, cloves.")

class ChaiShop:
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()

class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai

shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai.add_spices()
```

---

## 🧩 Step-by-step Explanation

### 1. **Base class `BaseChai`**

```python
class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai....")
```

* `BaseChai` is the **parent class** for all chai types.
* `prepare()` is a **method shared** by all chai types.

---

### 2. **Subclass `MasalaChai`**

```python
class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardamom, ginger, cloves.")
```

* Inherits from `BaseChai` → gets `__init__` and `prepare()` automatically.
* Adds a **new method** `add_spices()` unique to Masala chai.

---

### 3. **Class attribute in `ChaiShop`**

```python
class ChaiShop:
    chai_cls = BaseChai
```

* `chai_cls` determines which type of chai the shop serves.
* Default: `BaseChai` (regular chai).

```python
def __init__(self):
    self.chai = self.chai_cls("Regular")
```

* When shop instance is created, it **creates a chai object** using `chai_cls`.

---

### 4. **Subclass `FancyChaiShop`**

```python
class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai
```

* Inherits everything from `ChaiShop`.
* Overrides `chai_cls` → now it serves `MasalaChai`.

---

### 5. **Execution**

```python
shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve()
```

✅ Output:

```
Serving Regular chai in the shop
Preparing Regular chai....
```

```python
fancy.serve()
```

✅ Output:

```
Serving Regular chai in the shop
Preparing Regular chai....
```

* Actually, fancy uses `MasalaChai` via `chai_cls` → so it prepares **MasalaChai**. (Type shows "Regular" because we passed `"Regular"` as type during initialization.)

```python
fancy.chai.add_spices()
```

✅ Output:

```
Adding cardamom, ginger, cloves.
```

* `MasalaChai` method is called, showing subclass-specific behavior.

---

## 🧠 Key Concepts

| Concept                  | Explanation                                            |
| ------------------------ | ------------------------------------------------------ |
| Inheritance              | `MasalaChai` inherits `BaseChai` methods/attributes    |
| Method addition          | Subclass can add new behavior (`add_spices`)           |
| Composition              | `ChaiShop` contains a `chai` object (`self.chai`)      |
| Class attribute override | `FancyChaiShop.chai_cls = MasalaChai` changes behavior |

---