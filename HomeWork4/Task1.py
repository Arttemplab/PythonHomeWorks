#Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
# If the string length is less than 2, return instead of the empty string.

s = 'Mi is a cow and she makes My'
if len(s) < 2:
    result = ''
else:
    result = s[:2] + s[-2:]
print(result)