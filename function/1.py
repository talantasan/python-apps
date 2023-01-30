def salam():
    print('Hello World from Talant')
    
salam()

# value inside function
name = 'Talant'
def greeting(name):
    print('Hello '+name)

greeting(name)

# int value as an example
num1 = 34
def numfunc1(num1):
    print(12+num1)

numfunc1(num1)

# 
age = 40
name = 'Talant'

def mygreeting(age, name):
    print('Hello '+name+' you are '+str(age)+' years old')
    
mygreeting(age, name)

# passing multiple values
def greeting1(*custnames):
    print('Hello '+custnames[1])
    
greeting1('Talant, Aibek', 'Nurbek')
