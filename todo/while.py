user_prompt = "Enter todo list: "
todos = []

while True:
    todo = input(user_prompt)
    print(todo.capitalize())
    todos.append(todo)
    print(todos)
