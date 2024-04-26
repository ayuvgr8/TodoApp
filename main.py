# user_prompt = "Enter the todo:" todos = ['run', 'clean', 'throw']

# todos = []

while True:
    # Get User input and strip space characters into it
    user_action = input("Type Add, Show, Edit, Complete, Exit : ")
    user_action = user_action.strip()  # strip() function is used to eliminate the extra spaces

    # check if the user action is "Add"
    # Needs to use meaningful variable name to avoid lots of comments

    # ADD FUNCTION

    if user_action.startswith("add") or user_action.startswith("new") or user_action.startswith("more"):
        # new_line = '\n'
        todo = (user_action[4:])  # Extracting the todo without the "add" keyword

        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        # todos.append(new_line + todo)
        todos.append(todo + '\n')
        # with open('todos.txt', 'a') as file:  # Open the file in append mode ('a')
        #     file.write(todo + '\n')  # Write the todo followed by a newline character

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    #  SHOWCASE

    elif user_action.startswith("show"):  # bitwise Operator (Show or Display type anything  )

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):  # enumerate fn used here to get index
            # item = item.strip('\n') Alternative of list- comprehension here
            item = item.title()
            row = f"{index + 1}.{item}"  # use of f"string" is here !
            print(row)



    # EDIT CASE
    # ERROR HANDLING
    elif user_action.startswith("edit"):  # we will use List Indexing Function
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1  # indexing the todo

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter the New Todo: ")
            todos[number] = new_todo.strip() + '\n'  # Append newline after new todo

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print(f"Your command is invalid for this user action : {user_action}")
            continue

            # COMPLETE / DELETE FUNCTION

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} has been removed from your list"
            print(message)
        except IndexError:
            print(f"There is no item with that Index {user_action}")
            continue

    # EXIT FUNCTION EXECUTED

    elif user_action.startswith("exit"):
        break
    else:
        print("Invalid Statement")

print("Byeeeeeeee!! You will be missed!")

todos.clear()  # Not sure why this line was here as todos variable is not used after this
# Comment added for testing
