# File Read & Write Challenge & Error Handling Lab

This project demonstrates how to work with files in Python, including reading, modifying, and writing files, as well as handling common errors such as file not found and permission issues.

## Features

1. **File Read & Write Challenge**:
    - The program reads content from an input file.
    - The content is modified (for example, converted to uppercase).
    - The modified content is written to a new output file.

2. **Error Handling Lab**:
    - The program prompts the user to enter a filename.
    - It handles errors gracefully if the file doesn't exist or can't be read.
    - Specific errors such as `FileNotFoundError` and `PermissionError` are handled.

## Technologies Used
- Python 

## How to Use

1. Clone or download this repository to your local machine.

2. **Modify an existing file**:
   - The program expects an input file named `example.txt` (or any file you specify in the code).
   - The program will read the file, modify its content (e.g., convert text to uppercase), and save it as a new file (e.g., `modified_example.txt`).

   **Steps**:
   - Ensure you have a file named `example.txt` in the same directory as the script.
   - Run the Python script (`file_read_write.py`).

3. **Handle errors when reading a file**:
   - The program will prompt you to enter the filename to read from the terminal.
   - If the file doesn’t exist or there's an issue with permissions, it will handle the error gracefully and display a relevant message.

   **Steps**:
   - When prompted, enter the filename you want to read from.
   - If the file exists and can be read, the program will display its content.
   - If there’s an issue (file not found, permission error), an error message will be displayed.

## Running the Program

To run the program, follow these steps:

1. Ensure you have Python 3.x installed on your computer.
2. Download or clone the repository to your local machine.
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the Python script by typing the following command:
   ```bash
   python file_read_write.py

Error: The file example.txt does not exist.
Error: You don't have permission to read the file filename.


---

This `README.md` provides clear documentation on how to use the program, how it works, and what errors it handles. Feel free to modify it based on any further details you'd like to add or customize!

