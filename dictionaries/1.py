mydict = {
    "name": "Talant",
    "lastname": "Karmyshakov",
    "age": 19,
    "male": True,
    "club": "GS",
    "fav_players": ['Zidane', 'Bati', 'RonaldoBR']
}

print(mydict)
print(mydict["club"])
print(mydict["fav_players"])

# duplicates are not allowed they are overwritten
mydict1 = {
    "name": "Talant",
    "lastname": "Karmyshakov",
    "lastname": "Asan",
    "club": "GS"
}
x = mydict["lastname"]
print(mydict1)
print(len(mydict1))
print(x)