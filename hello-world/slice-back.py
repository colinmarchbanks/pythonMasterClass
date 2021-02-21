letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[26:0:-1]
print(backwards) #should print the aplhabet backwards; actual: doesn't include a
print()

backwards = letters[26::-1]
print(backwards) #should print the aplhabet backwards

print()

backwards = letters[26:-27:-1]
print(backwards) #should print the aplhabet backwards; this one works too

print(letters[16:13:-1]) #qpo
print(letters[4::-1]) #edcba
print(letters[len(letters):len(letters)-9:-1]) #last 8 characters in reverse
