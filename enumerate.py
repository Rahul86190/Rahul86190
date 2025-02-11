#list enumeration

# enumerate() method adds a counter to an iterable and returns it in a form of enumerate object.
# This enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method.
# Syntax: enumerate(iterable, start=0)

string1="Global World"
print("string1:",string1)

enumerate_string1=list(enumerate(string1))
print("enumerate_string1:",enumerate_string1)

print("\n")
fruits=["Apple","Banana","Orange","Grapes"]
print("fruits:",fruits)

for index,fruit in enumerate(fruits):
    print("index:",index,"fruit:",fruit)

#enumerate = It is an inbuilt function that is used to iterate through the containers keeping track of the index.
print("\n")
enumerate_string1=tuple(enumerate(string1))
print("enumerate_string1:",enumerate_string1)

print("\n")
enumerate_string1=dict(enumerate(string1))
print("enumerate_string1:",enumerate_string1)