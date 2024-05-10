import sys

import functions.functions as fn

todos_filename = "todos.txt"
completedTodos_filename = "completed_todos.txt"

todo = ""
user_prompt = """
Possible inputs:
-> show,
-> completed
-> add followed by the todo,
-> edit followed by number of todo,
-> complete followed by the number
-> delete followed by number of todo,
-> exit
"""

fn.create_todos_file_if_not_exists(todos_filename)
fn.create_todos_file_if_not_exists(completedTodos_filename)

file = fn.read_todos_file(todos_filename)
print(file)
completed_file = fn.read_todos_file(completedTodos_filename)
print(completed_file)

todos = fn.convert_to_list(file)
completed_todos = fn.convert_to_list(completed_file)

while True:
    print(user_prompt)
    user_input = input(":")

    match user_input.lower().split()[0]:
        case "show":
            print("Things to do:")
            for index, todo in enumerate(todos):
                print(f"{index + 1} -> {todo}")

        case "completed":
            print("Things completed:")
            for index, todo in enumerate(completed_todos):
                print(f"{index + 1} -> {todo}")

        case "exit":
            print("Exiting the program...")
            sys.exit()  # This will exit the program

        case "add":
            _, *todo_words = user_input.split()
            todo = ' '.join(todo_words)
            todos.append(todo.title())
            print(f"Todo: {todo} added to the list")
            fn.save_todos_file(todos, todos_filename)

        case "complete":
            _, action = user_input.split()
            try:
                todo_index = int(action) - 1
                try:
                    todo_to_complete = todos[todo_index]
                    print(f"Marking \"{todo_to_complete}\" as completed")
                    completed_todos.append(todo_to_complete)
                    todos.remove(todo_to_complete)
                    fn.save_todos_file(completed_todos, completedTodos_filename)
                    fn.save_todos_file(todos, todos_filename)
                except IndexError:
                    print(f"Couldn't find a todo with number {todo_index + 1}")
            except ValueError:
                print("Could not parse an integer from the input string.")

        case "delete":
            _, action = user_input.split()
            try:
                todo_index = int(action) - 1
                try:
                    todo_to_delete = todos[todo_index]
                    print(f"Deleting: {todo_to_delete}")
                    todos.remove(todo_to_delete)
                    fn.save_todos_file(todos, todos_filename)
                except IndexError:
                    print(f"Couldn't find a todo with number {todo_index + 1}")
            except ValueError:
                print("Could not parse an integer from the input string.")

        case "edit":
            _, action = user_input.split()
            try:
                todo_index = int(action) - 1
                try:
                    todo_to_edit = todos[todo_index]
                    print(f"Editing: {todo_to_edit}")
                    new_todo = input(f"Enter new todo to replace \"{todo_to_edit}\": ")
                    todos[todo_index] = new_todo
                    fn.save_todos_file(todos, todos_filename)
                except IndexError:
                    print(f"Couldn't find a todo with number {todo_index + 1}")
            except ValueError:
                print("Could not parse an integer from the input string.")

        case _:
            print("Action not recognized, try again")
