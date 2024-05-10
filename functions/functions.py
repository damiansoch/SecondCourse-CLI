import os


def create_todos_file_if_not_exists(filename):
    """
    Checks if file exists and if not creates the file
    :param filename:str
    :rtype: None
    """
    # Check if the file exists
    if not os.path.exists(filename):
        # Create the file
        with open(filename, "w") as file:
            # Optionally, write some initial content to the file
            file.write("List of todos:\n")
        print("todos.txt created successfully.")
    else:
        print("todos.txt already exists.")


def read_todos_file(file_name):
    try:
        # Open the file in read mode
        with open(file_name, "r") as file:
            # Read the contents of the file line by line
            lines = file.readlines()
            print("Contents of", file_name, ":")
            for line in lines:
                print(line.strip())
            return lines
    except FileNotFoundError:
        print(file_name, "does not exist.")
        return None


def convert_to_list(todos_file):
    if todos_file is None:
        print("Error: File not found or unable to open.")
        return []  # Return an empty list if file is not valid

    todos_list = []

    # Read the contents of the file line by line
    for line in todos_file:
        # Append each line to the list, removing any trailing whitespace
        todos_list.append(line.strip())

    return todos_list


def save_todos_file(todos_list, filename):
    try:
        # Open the file in write mode, this will clear the file if it exists
        with open(filename, "w") as file:
            # Write each record from the list to the file, with each record on a new line
            for todo in todos_list:
                file.write(todo + "\n")

        print("todos.txt saved successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
