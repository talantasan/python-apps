todos = []

while True:
    user_action = input('Type add or show: ')
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input('Enter todos: ')
            todos.append(todo)
        case 'show' | 'display':
            for items in todos:
                items = items.title()
                print(items)
        case 'exit':
            break