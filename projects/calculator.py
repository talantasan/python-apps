x = int(input('Enter the first number: '))
y = int(input('Enter the second number: '))
op = input('Enter the operator from followings(+, -, *, /): ')

if op == '+':
    print('sum is '+str(x+y))
elif op == '-':
    print('difference is '+str(x-y))
elif op == '/':
    print('divisioin is '+str(x/y))
elif op == '*':
    print('sum is '+str(x*y))
else:
    print('you type wrong operator... Try again')