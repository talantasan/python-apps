class Customers:
    
    raise_amount = 1.05
    number_of_customers = 0 
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@talantzon.com'
        Customers.number_of_customers += 1

    def fullname(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    

cust1 = Customers('Talant', 'Karmyshakov', 5000)
cust2 = Customers('Samara', 'Ataeva', 6000)
cust3 = Customers('Meeriem', 'Asanbaeva', 13000)

# print(cust1.email)
# print(cust2.first)
# print(cust1.fullname())

cust1.raise_amount = 1.7

print(cust1.pay)
# Customers.apply_raise(cust1) or
cust1.apply_raise()
print(cust1.pay)

# To access the namespace of instance (in our case cust1 and cust2)
print(cust1.__dict__)
print(Customers.__dict__)
print(Customers.number_of_customers)
print(cust3.email)