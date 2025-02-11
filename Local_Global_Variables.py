Global_variable=10
print("Welcome to Local and Global Variables")

def local_variable():
    Local_variable=20
    print("Local Variable is:",Local_variable)
    global Global_variable
    print("Global Variable is:",Global_variable)
    print(globals())
    print("\n\n")
    print(locals())
    print()
    Global_variable =30   # changing the value of global variable 
    print("Global Variable is:",Global_variable)
local_variable()
print("Global Variable is:",Global_variable)

# print(globals())

