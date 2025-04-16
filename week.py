# file_rw.py

# Step 1: Open the original file and read contents
try:
    with open("input.txt", "r") as infile:
        content = infile.read()

    # Step 2: Modify the content
    modified_content = content.upper()  # You can change this to any transformation

    # Step 3: Write to a new file
    with open("output.txt", "w") as outfile:
        outfile.write(modified_content)

    print("File read and written successfully!")

except FileNotFoundError:
    print("The file 'input.txt' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
