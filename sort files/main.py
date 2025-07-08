import os
import shutil

folder_to_sort = ""
i = str(input("Enter your directory : to see what do you have in it:"))
root_folder = i

def showfiles():

    if not os.path.exists(root_folder):
        print("❌ Directory not found!")
        return

    for current_folder, subfolders, files in os.walk(root_folder):
        print(f"📁 Папка: {current_folder}")

        if subfolders:
            print("  📂 Підпапки:")
            for sub in subfolders:
                print(f"    - {sub}")

        if files:
            print("  📄 Файли:")
            for file in files:
                print(f"    - {file}")

        print("-" * 40)

try:
    showfiles()
except FileNotFoundError:
    print("Not found directory")