
user_guess = int(input("guess a number: "))

while (user_guess>9) or (user_guess<1):
    user_guess = int(input("guess a number: "))
else:
    print("Well Guessed")

