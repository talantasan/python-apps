myfile = open("/home/azureuser/python-apps/reading-files/countries.txt", "r")
for lines in myfile.readlines():
    print(lines)
myfile.close
