def write_f1():
    print('Enter the names of three friends: ')
    name1 = input('Enter 1st friend: ')
    name2 = input('Enter 2nd friend: ')
    name3 = input('Enter 3rd friend: ')
    
    friends = open('friends.txt', 'w')
    friends.write(name1+'\n')
    friends.write(name2+'\n')
    friends.write(name3+'\n')
    friends.close()

def read_f1():
    myfile = open('friends.txt', 'r')
    content1 = myfile.read()
    myfile.close()
    
    print(content1)
    
def friend_app():
    myfile = open('friends.txt', 'a')
    myfile.write('\nSamara is appended')
    myfile.close()

def main():
    write_f1()
    read_f1()
    friend_app()
main()