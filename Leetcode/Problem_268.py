def find_missing_num(nums):
	find_length = len(nums)

	for num in range(len(nums)+1):
		if num not in nums:
			return num

nums = [9,6,4,2,3,5,7,0,1]
print(find_missing_num(nums))

