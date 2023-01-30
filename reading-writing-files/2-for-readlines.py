myfile = open("/home/azureuser/python-apps/reading-files/talant.txt", "r")
for lines in myfile.readlines():
    print(lines)
myfile.close
