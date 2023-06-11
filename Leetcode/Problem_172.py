def factorial(n):
    total = 1
    while n>0:
        total*=n
        n-=1
    return total 

def findTrailingZeros(number):
    total = factorial(number)
    totalZeros = 0
    for idx in range(len(str(total))-1, -1, -1):
        if not str(total)[idx] == '0':
            break
        else:
            totalZeros+=1

    return totalZeros    

n = 12
totalZeros = findTrailingZeros(n)
print(totalZeros)