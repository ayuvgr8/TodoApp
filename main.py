# user_prompt = "Enter the todo:"

todos = []

while True:
    user_action = input("Type Add, Show, Edit or Exit : ")
    user_action = user_action.strip()                                            # strip() function is used to eliminate the extra spaces

    match user_action:
        case 'Add' | 'add':
            todo = input("Enter a Todo : ")
            todos.append(todo)
        case 'Show' | 'Display' | 'show' | 'display':                            # Bitwise Operator (Show or Display type anything  )
            for item in todos:
                item = item.title()
                print(item)
        case 'edit' | 'Edit':
            number = int(input("Number of the todo to edit: "))                  # we will use List Indexing Function
            number = number -1
            new_todo = input("Enter the New Todo: ")
            todos[number] = new_todo
        case 'Exit' | 'exit':
            break
        case  _:
            print("Hey! You entered an invalid input(unknown command) please try again")

print("Byeeeeeeee!! You will be missed!")

todos.clear()



