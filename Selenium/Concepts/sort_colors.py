nums = [2,9,6,1,3,8,5]
length = len(nums)

while length > 1 :
    for count in range(length-1):
        if nums[count] > nums[count+1] :
            nums[count],nums[count+1] = nums[count+1],nums[count]
    length -= 1        
print(nums)          # Bubble sort 