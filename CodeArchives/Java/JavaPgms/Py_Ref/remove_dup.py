array = [2,3,4,4,8,7,9,12,7,12,13]
res_array = []

for num in array:
    if num not in res_array:
        res_array.append(num)

print(res_array)        
