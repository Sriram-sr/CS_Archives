def find_recursively(num):
    if num == 1 :
        return num
    else :
        result = num * find_recursively(num-1)    
    return result

num = 5
print(find_recursively(num))        