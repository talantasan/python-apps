class Products:
    def __init__(self, pname, price):
        self.pname = pname
        self.price = price 

pr1 = Products('apple', 12)
pr2 = Products('soda', 5)

print(pr1.pname)
print(pr1.price)