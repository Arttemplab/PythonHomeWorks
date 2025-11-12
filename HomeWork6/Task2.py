# Exclusive common numbers.
# Generate 2 lists with the length of 10 with random integers from 1 to 10,
# and make a third list containing the common integers between the 2 initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers

import random

l = []
m = []
z = []
i = 0

while i < 10:
    l.append(random.randint(1, 10))
    m.append(random.randint(1, 10))
    i += 1

print(l)
print(m)
set_l = set(l)
set_m = set(m)
z = list(set_l & set_m)
print(z)


