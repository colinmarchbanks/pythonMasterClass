for i in range(1,13):
    print("No. {0:2} square is {1:3} and cubed is {2:4}".format(i,i ** 2, i ** 3)) # adding a width parameter to the formatting will allow you to take up a predefined amount of space

print()

for i in range(1,13):
    print("No. {0:2} square is {1:<3} and cubed is {2:^4}".format(i,i ** 2, i ** 3)) # < acts as a left alignment; ^ acts as centering

print()

print("Pi is approximately {0:12}".format(22 / 7))
print("Pi is approximately {0:12f}".format(22 / 7))
print("Pi is approximately {0:12.50f}".format(22 / 7))
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:72.50f}".format(22 / 7)) #python's ints are useless after 50 decimal points

age = 24
print("My age is %d years" % age)

major = "years"
minor = "months"

print("My age is %d %s, %d %s" % (age, major, 6,minor))
print("PI is approximately %f" % (22/7))
print("PI is approximately %60.50f" % (22/7))
