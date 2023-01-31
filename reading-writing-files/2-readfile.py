def main():
    myfile1 = open("newfile1.txt", "r")
    content1 = myfile1.read()
    myfile1.close()
    print(content1)
    
main()