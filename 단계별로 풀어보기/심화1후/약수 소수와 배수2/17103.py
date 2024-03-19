import math

n = int(input())

def cal_prime(num):
    prime = set()
    for i in range(2, num+1):
        if is_prime(i):
            prime.add(i)
    return prime
    
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def count_combinations(num, prime):
    count = 0
    for i in prime:
        if num - i in prime:
            count += 1
    return count

for _ in range(n):
    num = int(input())
    prime = cal_prime(num)
    count_result = count_combinations(num, prime)
    
    if count_result % 2 == 0:
        print(count_result // 2)
    else:
        print((count_result + 1) // 2)
