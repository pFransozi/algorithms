from pathlib import Path

folder = Path("new_dir")
folder.mkdir(exist_ok=True)

file = folder / "new_file.txt"

file.write_text("Hello, world")

file.read_text()