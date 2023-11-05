test_list = [2,3,7,9,3,4,1]
# result should be [2,3]
target = 16
res_list = []

for char in range(len(test_list)-1):
    if sum(test_list[char:char+2]) == target:
        res_list.append(test_list[char])
        res_list.append(test_list[char+1])

print(res_list)        