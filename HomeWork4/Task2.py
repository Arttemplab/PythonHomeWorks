#Write a program that asks the answer for a mathematical expression,
# checks whether the user is right or wrong,
# and then responds with a message accordingly.

math_expr = '2+2*2'
correct_answer = 6
user_answer = 6
if user_answer == correct_answer:
    print(f'Yes, {math_expr} is eqal to 6')
else:
    print(f' It isn\'t right answer')