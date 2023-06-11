def get_to_single_digit(num):
	while True:
		num = sum([int(digit) for digit in str(num)])
		if len(str(num))==1:
			return num

num = 939
print(get_to_single_digit(num))

