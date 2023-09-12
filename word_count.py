from pathlib import Path


def execute(path):
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"file not found {path}")
    else:
        words = contents.split()        
        num_words = len(words)
        print(f"num words {num_words}, file {path}")


files = ["text_files/alice.txt", "text_files/learning_python.txt", "text_files/test/txt"]

for file in files:
    path = Path(file)
    execute(path)
