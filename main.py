# user_prompt = "Enter the todo:" todos = ['run', 'clean', 'throw']

# todos = []

while True:
    # Get User input and strip space characters into it
    user_action = input("Type Add, Show, Edit, Complete, Exit : ")
    user_action = user_action.strip()  # strip() function is used to eliminate the extra spaces

    # check if the user action is "Add"
    # Needs to use meaningful variable name to avoid lots of comments
    if 'add' in user_action:
        # it will show the string
        todo = user_action[2:]

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:  # bitwise Operator (Show or Display type anything  )

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):  # enumerate fn used here to get index
            # item = item.strip('\n') Alternative of list- comprehension here
            item = item.title()
            row = f"{index + 1}.{item}"  # use of f"string" is here !
            print(row)

    elif 'edit' in user_action:  # we will use List Indexing Function

        number = int(input("Number of the todo to edit: "))  #  we are converting str to int here
        number = number - 1  # indexing the todo

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter the New Todo: ")
        todos[number] = new_todo  # access the items from the list and how to replace that item through that syntax

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'complete' in user_action:
        number = int(input("Number of the todo to complete: "))

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        index = number - 1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"Todo {todo_to_remove} has been removed from your list"
        print(message)

    elif 'Exit' in user_action:
        break

print("Byeeeeeeee!! You will be missed!")

todos.clear()
