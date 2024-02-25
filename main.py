# user_prompt = "Enter the todo:"

todos = []

while True:
    user_action = input("Type Add, Show or Exit : ")
    user_action = user_action.strip()  #strip() function is used to eliminate the extra spaces

    match user_action:
        case 'Add' | 'add':
            todo = input("Enter a Todo : ")
            todos.append(todo)
        case 'Show' | 'Display' | 'show' | 'display':   #Bitwise Operator (Show or Display type anything  )
            for item in todos:
                item = item.title()
                print(item)
        case 'Exit' | 'exit':
            break
        case  _:
            print("Hey! You entered an invalid input(unknown command) please try again")

print("Byeeeeeeee!! You will be missed!")

todos.clear()



