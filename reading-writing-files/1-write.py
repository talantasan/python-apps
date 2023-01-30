# overwrites existing one or creates new file
myfile = open("/home/azureuser/python-apps/reading-writing-files/talant.txt", "w")
myfile.write('New text is adding')
myfile.close


# append a new line to the existing file
myfile = open("/home/azureuser/python-apps/reading-writing-files/talant.txt", "a")
myfile.write('\nSecond new  text is adding')
myfile.close

# create a new python file
myfile = open("/home/azureuser/python-apps/reading-writing-files/newpython.py", "w")
myfile.write('print(\'Hello World \')')
myfile.close
