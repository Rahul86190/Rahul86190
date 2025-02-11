print("hello my name is rahul") # hello my name is rahul
print("Enter for  Continue")
input() # Enter Continue

print("My age is 20") # My age is 20
print("I am a student") # I am a student
print("Enter for  Continue")
input() # Enter Continue

print("I am a student of B.Tech") # I am a student of B.Tech
print("I am a student of Computer Science") # I am a student of Computer Science
print("Enter for  Continue")
input() # Enter Continue

print("I am a student of Computer Science in 3rd year") # I am a student of Computer Science in 3rd year
print("I am a student of Computer Science in 3rd year in B.Tech") # I am a student of Computer Science in 3rd year in B.Tech

dic={'name':'rahul','age':20,'class':'btech'}
dic["school"]="DPS"
dic["city"]="Delhi"
print(dic)

print(len(dic))
#len(dic) returns the number of items in the dictionary.
#here the dictionary dic has 5 items so it will return 5
# 5 items are name, age, class, school, city

print(str(dic))
#str(dic) returns the string representation of the dictionary.
print(str(dic)[0])

a=dict.fromkeys(dic)
print(a)
#dict.fromkeys(dic) returns a new dictionary with keys from dic and values set to None. 

b=dict.fromkeys(dic,10)
print(b)
#dict.fromkeys(dic,10) returns a new dictionary with keys from dic and values set to 10.
