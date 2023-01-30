try:
    myfile = open("/home/azureuser/python-apps/reading-files/countries.txt", "r")
    print(myfile.readlines()[1])
    # print(myfile.readlines()[3])
    # print(myfile.readline())
    # print(myfile.readlines())
    myfile.close

except :
    print('Something went wrong')
    
finally:
    print('End of process')
    
# --------------------------------------------------------------------------------
