def string_quotes():
    print("hello 'rahul'")
    print('hello "rahul"')

    print('Hello Rahul\'s Sister')

    print('''Hello Rahul's Sister. My name is "Rihana"''')


    print("Hello Rahul's Sister. My name is \"Rihana\"")
    string_quotes()

def string_write():
    print("c:\\newfolder\\newfile.txt") # c:\newfolder\newfile.txt

    print("Hello\nRahul") # Hello

    print("Hello\tRahul") # Hello    Rahul
string_write()

def string_concatenation():
    print("ASCII value of A is",ord('A')) # ASCII value of A is 65

    # ord() function is used to get the ASCII value of a character

    print("Character of ASCII value 65 is",chr(65)) # Character of ASCII value 65 is A
    # chr() function is used to get the character of ASCII value

    print("ASCII number of character \x42 is: ",ord("\x42")) # ASCII number of character B is: 66
    # \x42 is a hexadecimal representation of ASCII value of character B

    print("ASCII value of 42 is: ",chr(66)) # ASCII number of character B is: B

    print(ord("#"))  # cahr to ASCII value
    print(chr(11))    # ASCII value to char
string_concatenation()

string_formatting():
    name="Rahul"
    age=20
    print("Hello",name,"your age is",age) # Hello Rahul your age is 20

    print("Hello "+name+" your age is "+str(age)) # Hello Rahul your age is 20

    print("Hello {} your age is {}".format(name,age)) # Hello Rahul your age is 20

    print("Hello {0} your age is {1}".format(name,age)) # Hello Rahul your age is 20

    print(f"Hello {name} your age is {age}") # Hello Rahul your age is 20
string_formatting()