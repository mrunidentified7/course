a = int(input('Кубик Кости: '))
b = int(input('Кубик владельца: '))
if a >= b:
	rasn = a-b
	print('Разность:', rasn)
	print('Игрок платит.')
else:
	summ = a+b
	print('Сумма:', summ)
	print('Владелец платит.')
	print('Игра окончена.')
	
