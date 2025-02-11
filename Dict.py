# for loop in dict

dict={'name':'zara','age':7,'class':'first'}

for key in dict:
    print((dict[key]))
print("\n\n")

for key in dict.keys():
    print(key)
print("\n\n")

for value in dict.values():
    print(value)
print("\n\n")

for key,value in dict.items():
    print(key,value)
