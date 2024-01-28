xp = int(input('Введите количество опыта: '))

if xp >= 1 and xp < 1000:
    print('Ваш уровень: 1')
elif xp >= 1000 and xp < 2500:
    print('Ваш уровень: 2')
elif xp >= 2500 and xp < 5000:
    print('Ваш уровень: 3')
elif xp >= 5000:
    print('Ваш уровень: 4')
