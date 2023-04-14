password = input('Enter password: ')
cnt = 1
while password != 'pass123':
    password = input('Enter password: ')
    cnt += 1
    if cnt > 2:
        print('Tries exceeded... Try again later.')
        break
print('Password is correct')
