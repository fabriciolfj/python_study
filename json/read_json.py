from pathlib import Path
import json


path = Path("numbers.json")
contents = path.read_text(encoding="utf-8")

result = json.loads(contents)
print(result)