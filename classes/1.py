class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp1 = Employee('talant', 'karmyshakov', 3000)
emp2 = Employee('samara', 'ataeva', 4000)

# print(emp1.email)
# print(emp2.email)

# print('{} {}'.format(emp1.first, emp1.last))
# created new method for displaying fullname, we can call by:

print(emp1.fullname()) 

# we also can pass by Classname
print(Employee.fullname(emp2))