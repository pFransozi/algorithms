import os

if not os.path.exists("new_dir"):
    os.makedirs("new_dir")

file = os.path.join("new_dir", "new_file.txt")

with open(file, "w") as f:
    f.write("Hello, world")

with open(file, "r") as f:
    print(f.read())