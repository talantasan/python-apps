x = 2
y = 6
z = 4

if (x>y) and (y>z):
    print(str(x)+' is greatest')
elif (y>z):
    print(str(y)+' is the greatest')
elif (x == y) and (y == z):
    print('All are equal')
else:
    print(str(z)+' is the greatest')  