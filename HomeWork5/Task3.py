#Create a program that reads an input string and then creates and prints 5 random strings
# from characters of the input string.
#For example, the program obtained the word ‘hello’, so it should print 5 random strings(words)
# that combine characters
#'h', 'e', 'l', 'l', 'o' -> 'hlelo', 'olelh', 'loleh' …

import random
my_string = input("Write your string and press Enter button: ")
for i in range(5):
   r_string = random.sample(my_string, len(my_string))
   print(''.join(r_string))