from pathlib import Path
import json


numbers = [1, 2, 5, 6]
values = json.dumps(numbers)

path = Path("numbers.json")
path.write_text(values)
