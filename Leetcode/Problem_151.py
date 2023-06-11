def reverse_line(string):
    splitted_list = string.split()
    reversed_list = reversed(splitted_list)
    output_string = ' '.join(reversed_list)

    return output_string

    
s = "  hello world  "    
# print(reverse_line(s))


def find_max_product(nums):
    products = []

    for idx in range(len(nums)-1):
        products.append(nums[idx]*nums[idx+1])

    max_value = max(products)
    
    return max_value

nums = [0, 2]
# print(find_max_product(nums))

def findPeakElement(nums):
        max_idx = 0
        max_value = nums[0]

        for idx in range(len(nums)):
            if nums[idx] > max_value:
                max_idx = idx
            max_value = nums[idx] 

        return max_idx            

nums = [1,2,1,3,5,6,4]
# print(findPeakElement(nums))   

def max_gap(nums):
    if len(nums)==1:
        return 0
    nums.sort()
    difference_list = []

    for idx in range(len(nums)-1):
        difference_list.append(abs(nums[idx]-nums[idx+1]))

    return max(difference_list)

nums = [3,6,9,1]
print(max_gap(nums))


