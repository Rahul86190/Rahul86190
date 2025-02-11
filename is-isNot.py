a=20
b=a
print("a=",a, "id(a): ",id(a), "b=",b, "id(b): ",id(b))
if(a==b):
    print("Both are same")
else:
    print("Both are different")

if(id(a)==id(b)):
    print("Identity of Both are same")
else:
    print("Identity of Both are different")

b=50
print("a=",a, " id(a)= ",id(a), "b=",b, " id(b): ",id(b))
if(a==b):
    print("Both are same")
else:
    print("Both are different")

if(id(a)==id(b)):
    print("Identity of Both are same")
else:
    print("Identity of Both are different")