# user_prompt = "Enter the todo:"

todos = []

while True:
    user_action = input("Type Add, Show or Exit : ")
    user_action = user_action.strip()

    match user_action:
        case 'Add':
            todo = input("Enter a Todo : ")
            todos.append(todo)
        case 'Show' | 'Display':
            for item in todos:
                print(item)
        case 'Exit':
            break
        case  _:
            print("Hey! You entered an invalid input(unknown command) please try again")

print("Byeeeeeeee!! You will be missed!")



