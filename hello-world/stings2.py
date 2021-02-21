parrot = "Norwegian Blue"

print(parrot)

print(parrot[3]) #using brackets on the string will target the character located at that index, like an array of characters

#mini challenge
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()

print(parrot[-1]) #13
print(parrot[-14]) #1

print()

#mini challenge 2
print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print()

#mini challenge
print(parrot[3 - len(parrot)])
print(parrot[4 - len(parrot)])
print(parrot[9 - len(parrot)])
print(parrot[3 - len(parrot)])
print(parrot[6 - len(parrot)])
print(parrot[8 - len(parrot)])

print()

print(parrot[0:6]) #Norweg

print(parrot[3:5]) #we
print(parrot[7] + parrot[2] + parrot[4]) # are
print(parrot[0:9]) #Norwegian

print(parrot[10:14]) #blue; Theres no index out of bounds error?
print(parrot[10:])

print(parrot[:9]) #Norwegian
print(parrot[10:]) #Blue

print(parrot[:]) #Norwegian Blue


print(parrot[-4:-2]) #Bl
print(parrot[-4:12]) #Bl

#Steps, the 3 variable in the parameter will be the numbers that are counted, like a jump
print(parrot[0:6:2]) #Nre
print(parrot[0:6:3]) #Ne

number = "1.123,333,222,123,120"
print(number[1::4]) # all commas and the decimal
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])