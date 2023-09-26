import re 
str1 = 'Talantbek Karmyshakov association passoc'

response = re.search(r'assoc', str1)
print(response.group())
