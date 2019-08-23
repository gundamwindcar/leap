def is_leap(y):
	if y % 4 != 0:
		return False
	elif y % 4 == 0 and y % 100 != 0:
		return True
	elif y % 100 == 0 and y % 400 != 0:
		return False
	elif y % 400 == 0 and y % 3200 != 0:
		return True

year = input('Please enter the year:')
year = int(year)
result = is_leap(year)
if result == True:
	print('This is a leap year.')
else:
	print('This is not a leap year.')