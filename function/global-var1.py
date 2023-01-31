num1 = 100

def main():
    global num1 # you have to define as global to change global value, it is no suggested to use global variables
    num1 = int(input('Enter a new number: '))
    show_value(num1)
def show_value(arg1):
    print(arg1)
    
main()
print(num1)