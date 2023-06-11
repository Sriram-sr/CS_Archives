def removeKdigits(num: str, k: int) -> str:
	min_list = []

	for idx in range(len(num)):
		temp_string = num[:idx] + num[idx+k:]
		if temp_string=='':
			min_list.append(0)
		else:	
		    min_list.append(int(temp_string))

	return str(min(min_list))

num = "10200"
k = 1
print(removeKdigits(num,k))
