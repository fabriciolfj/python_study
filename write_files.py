from pathlib import Path

contents = "meu nome e fabricio\n"
contents += "moro no interior de sp\n"

file = Path("text_files/meus_dados.txt")
file.write_text(contents)
