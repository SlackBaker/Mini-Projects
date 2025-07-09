import os
import shutil

class FindFiles:
    def __init__(self):
        self.root_folder = str(input("Enter root folder:"))

    def showfiles(self):
        if not os.path.exists(self.root_folder):
            print(" Directory not found!")
            return

        for current_folder, subfolders, files in os.walk(self.root_folder):
            print(f" Folder: {current_folder}")

            if subfolders:
                print("   Subfolders:")
                for sub in subfolders:
                    print(f"    - {sub}")

            if files:
                print("   Files:")
                for file in files:
                    print(f"    - {file}")

            print("-" * 40)

# --- Головний код (поза класом) ---
try:
    finder = FindFiles()
    finder.showfiles()
except Exception as e:
    print(f" Error: {e}")

class move_summver:
    def __init__(self):
        self.from_folder = str(input("Enter from where you want to move files"))
        self.to_folder = str(input("to:"))
        self.files = str(input("Prefics to move:"))

    def move_files(self):
        pass
