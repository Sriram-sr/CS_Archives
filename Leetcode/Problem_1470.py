def shuffle_array(nums, n):
	commmon_list = []
	start = nums[:n]
	end = nums[n:]
	for num in range(n):
		commmon_list.append(start[num])
		commmon_list.append(end[num])
	print(commmon_list)	

nums = [2,5,1,3,4,7]
n = 3
shuffle_array(nums, n)
