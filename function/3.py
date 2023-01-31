def main():
    value = 99
    print('The value is ',value)
    change_val(value)
    print('Back in main the value is ', value)
    
def change_val(arg1):
    print('Value is changing')
    arg1 = 0
    print('Now the value is ', arg1)

main()
    
    