for i in range(2,5):
    print(i)
    
# continue
for i in range(10, 100, 10):
    if i == 80:
        continue
    print(i)
    
# break
for i in range(10, 100, 10):
    if i == 80:
        break
    print(i)

# else in for
for i in range(10):
    print(i)
else:
    print("Loop finished")

    