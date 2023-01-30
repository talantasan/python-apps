numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'strawberry']

numbers.extend(fruits)
print(numbers)

# End the value to the end of a list
fruits.append('mango')
print(fruits)
print(len(fruits))

# Value in btw list 
numbers.insert(4,'x')
print(numbers)

# remove from the list
numbers.remove('apple')
print(numbers)

# delete list
numbers.clear()
print(numbers)

