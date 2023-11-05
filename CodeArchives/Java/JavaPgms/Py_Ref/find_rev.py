array = [2,4,5,6,19,7,8,]
length = len(array)//2

for char in range(length):
    last = len(array)-1-char
    temp = array[char]
    array[char] = array[last]
    array[last] = temp

print(array)    