for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i**2, i**3))
    print("*"*80)

name = input("Please enter your name: ")
age = int(input("How old are you,{0}? ".format(name))) #converting an input to an int can be useful but will crash of you input NaN
print(age)

if age >= 18:
    print("You are old enough to vote")
    print("Please out an X in the box")
else:
    print("Please come back in {0} years!".format(18-age))