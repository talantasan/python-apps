import random 

def main():
    for count in range(1, 10):
        number = random.randint(1, 100)
        print(number)
    my_random(5, 10)

def my_random(arg1, arg2):
    rand1 = random.randrange(arg1, arg2)
    print('this is from randrange ', rand1)

main()

