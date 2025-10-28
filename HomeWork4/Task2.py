#Make a program that checks if a string is in the right format for a phone number.
# The program should check that the string contains only numerical characters and is only 10 characters long.
# Print a suitable message depending on the outcome of the string evaluation.

num = '8095777777'
if num.isdigit() and len(num) == 10:
    print(f"{num} is a valid phone number.")
else:
    print(f"{num} is an invalid phone number.")