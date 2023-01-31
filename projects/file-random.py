import random

def main():
    random_numbers_file()
    
def myrandom():
    mylist = []
    for i in range(1, 11):
        x = random.randint(1, 20)
        mylist.append(x)
    return mylist

def random_numbers_file():
    new_list = myrandom()
    newfile = open('randomnumbers.txt', 'w')
    for i in new_list:
        newfile.write(str(i)+'\n')
    newfile.close()
    
main()