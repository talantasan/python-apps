def main():
    myfile = open('numbers.txt', 'w')
    num1 = int(input('Enter 1st number: '))
    num2 = int(input('Enter 2nd number: '))
    num3 = int(input('Enter 3rd number: '))
    
    myfile.write(str(num1)+'\n')
    myfile.write(str(num2)+'\n')
    myfile.write(str(num3)+'\n')
    myfile.close()
    readnow()
    
    
def readnow():
    myfile = open('numbers.txt', 'r')
    content1 = myfile.read() 
    myfile.close()
    print(content1)

main()