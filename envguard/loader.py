import os

def load_dotenv(dotenv_path: str = ".env"):
    if not os.path.exists(dotenv_path):
        return

    with open(dotenv_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            if "=" not in line:
                continue

            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip())
