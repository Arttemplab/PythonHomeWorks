name ='Artem'
day = 'Friday'
print(f'Good day {name}! {day} is a perfect day to learn some python.')
print('Good day {0}! {1} is a perfect day to learn some python.'.format(name, day))
sentence = 'Good day {}! {} is a perfect day to learn some python.'
print(sentence.format(name,day))
print('Good day %s! %s is a perfect day to learn some python.'% (name, day))

