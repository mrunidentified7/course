hours = int(input('Введите отработанные часы: '))
debt = int(input('Введите остаток по кредиту: '))
eat = int(input('Введите траты на еду: '))
salary = 200*hours//2**3+hours
summ = debt+eat
if salary >= summ:
	print('Часов хватает. Можно отдохнуть.')
else:
	print('Часов не хватает. Придется работать больше!')
	
