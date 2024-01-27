price1 = int(input('Первый товар: '))
price2 = int(input('Второй товар: '))
price3 = int(input('Третий товар: '))
summ = price1+price2+price3
if summ > 10000:
	discount = summ*10//100
	print('Цена со скидкой:', summ-discount)
else:
	print('Цена:', summ)
