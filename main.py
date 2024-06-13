# Initialize an empty todos list
# todos = []

while True:
    # Get user input and strip space characters
    user_action = input("Type Add, Show, Edit, Complete, Exit: ")
    user_action = user_action.strip().lower()  # strip() eliminates extra spaces, lower() handles case insensitivity

    # ADD FUNCTION
    if user_action.startswith("add") or user_action.startswith("new") or user_action.startswith("more"):
        todo = user_action[4:].strip()  # Extracting the todo without the "add" keyword and stripping any extra spaces
        if todo:  # Ensure todo is not empty
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo + '\n')

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        else:
            print("Please provide a valid todo item.")

    # SHOWCASE
    elif user_action.startswith("show"):
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todos = [item.strip() for item in todos]

        for index, item in enumerate(new_todos):
            item = item.title()
            row = f"{index + 1}. {item}"
            print(row)

    # EDIT FUNCTION
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:].strip())
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            if 0 < number <= len(todos):
                new_todo = input("Enter the new todo: ").strip()
                if new_todo:  # Ensure new todo is not empty
                    todos[number - 1] = new_todo + '\n'

                    with open('todos.txt', 'w') as file:
                        file.writelines(todos)
                else:
                    print("Please provide a valid todo item.")
            else:
                print("Invalid number. Please try again.")
        except ValueError:
            print("Invalid command. Please enter a valid number.")
        except IndexError:
            print("Invalid index. Please enter a valid number.")

    # COMPLETE/DELETE FUNCTION
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:].strip())
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            if 0 < number <= len(todos):
                todo_to_remove = todos.pop(number - 1).strip()

                with open('todos.txt', 'w') as file:
                    file.writelines(todos)

                message = f"Todo '{todo_to_remove}' has been removed from your list."
                print(message)
            else:
                print("Invalid number. Please try again.")
        except ValueError:
            print("Invalid command. Please enter a valid number.")
        except IndexError:
            print("Invalid index. Please enter a valid number.")

    # EXIT FUNCTION
    elif user_action.startswith("exit"):
        break
    else:
        print("Invalid command. Please try again.")

print("Bye! You will be missed!")

# No need to clear the todos list as the program is ending
