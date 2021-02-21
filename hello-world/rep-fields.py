age = 25
print("My age is " + str(age) + " years") # using the str() function will allow us to bind the value as a string, this is replaced in python 3

#python 3

print("My age is {0} years".format(age))

print("""Jan {2}
Feb {0}
Mar {1}
Apr {2}
May {1}
Jul {2}
Aug {1}
Sep {2}
Nov {1}
Dec {2}""".format(28,30,31))
