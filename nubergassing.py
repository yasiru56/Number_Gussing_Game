import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('pleace type a number larger than 0 next time')
        quit()

else:
    print('Please type a nuber next time.')
    quiet()


random_number = random.randint(0,top_of_range)
guesses = 0

while True:
    guesses +=1
    user_guess = input("Mark a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('please type a number next time.')
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:   
        print("You were above the nuber!")
    else:
        print("you were below the nuber!")
print("you got it in",guesses,"guesses")    