todos = []
while True:
    x = input('Enter add, show, edit or stop: ')
    match x:
        case 'stop':
            break
        case 'show':
            for i in todos:
                print(i)
        case 'add':
            y = input('Enter todo: ')
            todos.append(y)
        case 'edit':
            num = int(input('Enter the number of todos to edit: '))
            num = num - 1
            todo = todos[num]
            new_todo = input('Enter new todo: ')
            todos[num] = new_todo

print(todos)