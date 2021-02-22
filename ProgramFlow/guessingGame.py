answer = 5;

print("Please guess a number between 1-10: ")
guess = int(input())

if(guess > answer):
    print("Sorry that is too high!")

elif (guess < answer):
    print("Sorry that is too low!")

else:
    print("Good job!")