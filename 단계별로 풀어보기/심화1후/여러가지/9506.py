def divisor(n):
    result = []
    count = 0
    for i in range(1,n):
        if n%i == 0:
            result.append(i)
            count += i
    return result, count
while True:
    n = int(input())
    if n == -1:
        break
    divisorList, divisorSum = divisor(n)
    if n == divisorSum :
        print(f"{n} = {' + '.join(map(str, divisorList))}")
    else:
        print(f"{n} is NOT perfect.")

          