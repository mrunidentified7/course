rating = int(input('Что получил по математике? '))
def rating_bad():
	print('Плохо. Марш учиться!')
def rating_good():
	print('Молодец! Можешь отдохнуть.')
if rating == 2 or rating == 3:
	rating_bad()
elif rating == 4 or rating == 5:
	rating_good()
