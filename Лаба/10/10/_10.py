import random
i=random.randint(1,10)
a=int(input('Угадай число от 1 до 10, пока не поймешь правильно:'))
while a!=i:
    a=int(input('Угадай число от 1 до 10, пока не поймешь правильно:'))

print('Хорошо угадали!')