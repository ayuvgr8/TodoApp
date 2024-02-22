user_prompt = "Enter the todo:"

todos = []

while True:
    todo = input(user_prompt)
    print(todo.title())
    todos.append(todo)
