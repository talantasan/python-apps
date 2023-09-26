class Customers:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@talantzon.com'

    def fullname(self):
        return f'{self.first} {self.last}'
    

cust1 = Customers('Talant', 'Karmyshakov', 5000)
cust2 = Customers('Samara', 'Ataeva', 6000)

print(cust1.email)
print(cust2.first)
print(cust1.fullname())

