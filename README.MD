# envguard

**Minimal and safe environment variable validator and loader for Python apps**

---

## ✅ Features
- Load environment variables from a `.env` file
- Validate presence and type of required variables
- Support default values for optional variables
- Built-in smart boolean parsing
- Clean and Pythonic API

---

## 📦 Installation
```bash
pip install envguard
```

> Or clone locally:
```bash
git clone https://github.com/yourusername/envguard.git
cd envguard
pip install .
```

---

## 🛠 Usage

### .env file:
```env
DB_HOST=localhost
DB_PORT=5432
DEBUG=true
```

### Python code:
```python
from envguard.loader import load_dotenv
from envguard import EnvGuard

load_dotenv()

config = EnvGuard({
    "DB_HOST": str,
    "DB_PORT": int,
    "DEBUG": (bool, False),        # optional with default
    "TIMEOUT": (float, 10.0)       # another optional var
}).load()

print(config.DB_HOST)    # 'localhost'
print(config.TIMEOUT)    # 10.0
```

---

## 🔍 Type Casting Rules
- `str`: unchanged
- `int`, `float`: cast directly
- `bool`: accepts `true/false`, `1/0`, `yes/no`, `on/off` (case-insensitive)

---

## ⚠️ Errors
- `MissingEnvVarError` – if a required var is missing
- `InvalidEnvVarTypeError` – if casting fails

---

## ✅ Testing
```bash
pytest
```

---

## 📜 License
MIT © Akshay Kumar
