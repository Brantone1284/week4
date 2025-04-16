# error_handling_lab.py

filename = input("Enter the filename to read: ")

try:
    with open(filename, "r") as file:
        print("File content:\n")
        print(file.read())
except FileNotFoundError:
    print("❌ File not found. Please check the name and try again.")
except PermissionError:
    print("❌ Permission denied. You can't access this file.")
except Exception as e:
    print(f"⚠️ Unexpected error: {e}")
