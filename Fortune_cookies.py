import random

lucky_number = random.randint(1,100)
fortune_number = random.randint(1,3)

fortune_text = ' '

if fortune_number == 1:
    fortune_text = 'You will have a great day!'
if fortune_number == 2:
    fortune_text = 'Today\'s gonna be a tough day ;-;... but YOU GOT THIS!!' 
if fortune_number == 3:
    fortune_text = 'You can expect a miraculous luck coming your way!'

print(f"{fortune_text} Your lucky number is:{lucky_number}")