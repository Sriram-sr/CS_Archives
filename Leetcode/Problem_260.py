nums = [-1,0]
unique_elements = []

for idx in range(len(nums)):
	if nums[idx] not in nums[:idx] and nums[idx] not in nums[idx+1:]:
		unique_elements.append(nums[idx])

print(unique_elements)		