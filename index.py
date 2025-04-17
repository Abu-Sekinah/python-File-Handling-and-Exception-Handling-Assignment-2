# Task 1: File Read & Write Challenge 🖋️
def modify_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as file:
            content = file.read()
            # Modify the content (for example, changing all text to uppercase)
            modified_content = content.upper()

        # Write the modified content to a new file
        with open(output_filename, 'w') as new_file:
            new_file.write(modified_content)
        print(f"File modified successfully and saved as {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Task 2: Error Handling Lab 🧪
def ask_for_file():
    filename = input("Please enter the filename to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content read successfully:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except PermissionError:
        print(f"Error: You don't have permission to read the file {filename}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main program to demonstrate both tasks
def main():
    # Task 1: Modify an existing file and write to a new one
    input_filename = 'example.txt'  # Replace with your file
    output_filename = 'modified_example.txt'
    modify_file(input_filename, output_filename)
    
    # Task 2: Ask user for a file and handle errors
    ask_for_file()

if __name__ == "__main__":
    main()
