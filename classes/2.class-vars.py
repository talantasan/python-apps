class Customers:
    
    raise_amount = 1.04
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
    
    @classmethod
    def set_raise_amnt(cls, amount):
        cls.raise_amount = amount
    
    @classmethod
    def parse_str_input(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    

cust1 = Customers('Talant', 'Karmyshakov', 5000)
cust2 = Customers('Samara', 'Ataeva', 6000)
cust3 = Customers.parse_str_input('Meeriem-Asanbaeva-13000')

Customers.set_raise_amnt(4)
print(cust1.pay)
cust1.apply_raise()
print(cust1.pay)
print(cust3.raise_amount)
print(cust3.first)