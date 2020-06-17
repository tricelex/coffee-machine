# put your python code here
# put your python code here
year = int(input())

is_leap = (year % 4 == 0) and (year % 100 != 0) or year % 400 == 0

if is_leap:
	print('Leap')
else:
	print('Ordinary')
