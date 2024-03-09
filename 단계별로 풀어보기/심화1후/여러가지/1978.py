import math
n = int(input())
prime = list(map(int,input().split()))
count = 0

def isPrime (n):
    global count
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

for i in prime:
    if isPrime(i):
        count +=1
    
print(count)