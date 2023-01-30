i =1 
while i < 6:
    print(i)
    i+=1

# for loop
for x in 'Talantbek':
    print(x)

# loops in list
list1 = ['ju', 'jo', 'jz']
for y in list1:
    print(y)
    

# loops in dictionaries
friends = {
    "name": ['Aibek', 'Munar', 'Kapar'],
    "age": 40
}

for j in friends:
    print(friends[j])

# break
list4 = [4, 6, 7, 3, 6]
for i in list4:
    if i == 3:
        break
    print(i)