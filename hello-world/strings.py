print("Today is a good day to learn python")
print('python is fun')
print("Python's strings are easy to use")
print('You can even use quotations in python! ("")')
print("hello" + " world")
greeting = "Hello"
name = input("Please enter a name ")

#comments comments comments

print(greeting + ' ' + name)

age = 25
print("age:",age)
print("type(age):",type(age))
age = "25"

print("age:",age)
print("type(age):",type(age))

print(name + f"'s age is {age}") #Section 3.36 example for f-strings, basically an alternative to replacement fields and the format function; problem with f-strings is it isnt backwards compatible with version 3.4 of python

# Python doesn't set the value of a variable, but rather rebinds the value of the variable to the new value that has been set equal to, no more binding functions

#Python 3 ints dont have a max value, so the computer will run out of memorary first :)))

a = 12
b = 3
print(a / b) #4.0 regular division
print(a // b) #4 interger division rounded down
print(a % b) #0 modulo divisio, remainder after the interger division

for i in range(1,a//b):
    print(i)