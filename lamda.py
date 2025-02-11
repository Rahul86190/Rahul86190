''' What is Lambda Function?
A lambda function is a small anonymous function.
An anonymous function is a function that is defined without a name.
While normal functions are defined using the def keyword in Python,small anonymous functions are defined using the lambda keyword.
A lambda function can take any number of arguments, but can only have one expression.
Syntax:
lambda arguments : expression
The expression is executed and the result is returned:
'''
# Example:

sum=lambda a,b:a+b
print(sum(5,10))