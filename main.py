# user_prompt = "Enter the todo:"

todos = []

while True:
    user_action = input("Type Add or Show : ")

    match user_action:
        case "Add":
            todo = input("Enter a Todo : ")
            todos.append(todo)
        case "Show":
            print(todos)



