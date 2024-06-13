# user_prompt = "Enter the todo:" todos = ['run', 'clean', 'throw']

# todos = []

while True:
    # Get User input and strip space characters into it
    user_action = input("Type Add, Show, Edit, Complete, Exit : ")
    user_action = user_action.strip()  # strip() function is used to eliminate the extra spaces

    match user_action:
        # check if the user action is "Add"
        # Needs to use meaningful variable name to avoid lots of comments
        case 'Add' | 'add':
            todo = input("Enter a Todo : ") + "\n"

            # file = open('todos.txt', 'r')
            # todos = file.readiness()
            # file.close()

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            # file = open('todos.txt', 'w')
            # file.writelines(todos)
            # file.close()

            with open('todos.txt', 'w') as file:
                file.writelines(todos)  

        case 'Show' | 'Display' | 'show' | 'display':  # bitwise Operator (Show or Display type anything  )

            # file = open('todos.txt', 'r')
            # todos = file.readlines()
            # file.close()

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            # new_todos = []

            # for item in todos:
            #    new_item = item.strip('\n')
            #    new_todos.append(new_item)

            # Inline for loop Alternative of upper commented function
            # List comprehension

            new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(new_todos):  # enumerate fn used here to get index
                # item = item.strip('\n') Alternative of list- comprehension here
                item = item.title()
                row = f"{index + 1}.{item}"  # use of f"string" is here !
                print(row)

        case 'edit' | 'Edit':  # we will use List Indexing Function

            # file = open('todos.txt', 'r')  # It Basically shows how to edit the file stores in Files
            # todos = file.readiness()
            # file.close()

            number = int(input("Number of the todo to edit: "))  # here  we are converting str to int here
            number = number - 1  # indexing the todo

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter the New Todo: ")
            todos[number] = new_todo  # access the items from the list and how to replace that item through that syntax

            # file = open('todos.txt', 'w')  # reformatted the file
            # file.writelines(todos)
            # file.close()

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("This Number of the todo to complete: "))

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} has been removed from your list"
            print(message)

        case 'Exit' | 'exit':
            break

        case _:
            print("Hey! You entered an invalid input(unknown command) please try again")

print("Byeeeeeeee!! You will be missed!")

todos.clear()
