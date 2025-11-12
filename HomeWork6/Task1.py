# The greatest number
# Write a Python program to get the largest number from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers


import  random

l = []
i = 0

while i < 10:
    l.append(random.randint(0, 1000))
    i += 1
print(l)
maxNumber = l[0]
i = 1
while i < len(l):
    if l[i] > maxNumber:
        maxNumber = l[i]
    i += 1
print("Largest number from a list:",  maxNumber)