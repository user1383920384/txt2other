import os

folder_path = "."

def convert_to(new_extension):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            base = os.path.splitext(filename)[0]
            new_file = f"{base}.{new_extension}"
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_file))
            print(f"{filename} -> {new_file}")

#EXAMPLE
def py():
    convert_to("py")

py() #and you will convert from .txt to .py
