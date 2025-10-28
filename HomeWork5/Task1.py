#Write a program that generates a random number between 1 and 10
# and lets the user guess what number was generated.
# The result should be sent back to the user via a print statement.

import random
print("Guess what number will be generated")
user_guess = int(input("Try to guess generated number, enter number from 1 to 10 and press Enter button: "))

computer = random.randint(1, 10)

if user_guess == computer:
    print(f'Cool! You guessed the right number, and it is {computer}')
else:
    print(f'Ypsss! The right number was {computer}')
