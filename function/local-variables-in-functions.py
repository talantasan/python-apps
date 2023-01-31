# main funciton definition
def main():
    print('the sum of 2 numbers: ')
    x = int(input('Enter first number: '))
    y = int(input('Enter second number: '))
    show_sum(x, y)
    
def show_sum(i,j):
    result = i+j
    print(result)
    
main()
