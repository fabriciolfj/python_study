from pathlib import Path

file = Path("/test/data.txt")

try:
    data = file.read_text(encoding="utf-8")
except FileNotFoundError:
    print("file not found")