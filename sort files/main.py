import os
import shutil

class FindFiles:
    def __init__(self):
        self.root_folder = str(input("Enter root folder:"))

    def showfiles(self):
        if not os.path.exists(self.root_folder):
            print("❌ Directory not found!")
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

class move_summver:
    def __init__(self):
        self.from_folder = str(input("Enter from where you want to move files"))
        self.to_folder = str(input("to:"))
        self.files = str(input("Prefics to move:"))

    def move_files(self):
        if not os.path.exists(self.from_folder):
            print(" Source directory not found!")
            return

        if not os.path.exists(self.to_folder):
            print(" Target directory not found! Creating...")
            os.makedirs(self.to_folder)

        found = False
        for file_name in os.listdir(self.from_folder):
            # Перевіряємо розширення, ігноруючи регістр
            if file_name.lower().endswith(self.files.lower()):
                full_file_name = os.path.join(self.from_folder, file_name)
                new_path = os.path.join(self.to_folder, file_name)

                print(f" Moving {file_name}")
                shutil.move(full_file_name, new_path)
                found = True

        if not found:
            print(" No files found with that prefix or extension!")

if __name__ == "__main__":


    while True:

        print("Menu")
        print("1. Show Files")
        print("2. Move Files")
        print("3. Exit")
        choice = int(input("Enter choice:"))
        if choice == 1:
            shower = FindFiles()
            shower.showfiles()
        elif choice == 2:
            mover = move_summver()
            mover.move_files()
        elif choice == 3:
            print("Shuting down...")
            break
        else:
            print("Invalid choice!")
