place = int(input('Введите место в списке поступающих: '))
points = int(input('Введите количество баллов за экзамены: '))
if place  <=10 and points>=290:
	print('Поздаравляем, вы поступили!')
	print('Бонусом вам будет начисляться стипендия.')
elif place <=10 and points<290:
	print('Поздаравляем, вы поступили!')
	print('Но вам не хватило баллов для стипендии.')
else:
	print('К сожалению вы не поступили.')
	