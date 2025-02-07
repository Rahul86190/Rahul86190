# To run this file from command prompt, use below command ✏
# python sys.py 10 20    (10 and 20 are arguments)
# ** you can pass any number of arguments at the run time  **

import sys
print("No of Arguments:",len(sys.argv))
print("List of Arguments:",sys.argv)
print("Argument 1:",sys.argv[0])
print("Argument 2:",sys.argv[1])
print("Argument 3:",sys.argv[2])
# print("Argument 4:",sys.argv[3])  # IndexError: list index out of range

first=int(sys.argv[1])
second=int(sys.argv[2])

print("Sum of",first,"and",second,"is",first+second)