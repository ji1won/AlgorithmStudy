n, b = map(int,input().split())
def deverse(n,b ) :
    if n == 0:
        return ''
    quotient, remain = divmod(n,b)
    
    if remain<10:
        remain_char = str(remain)
    else:
        remain_char= chr(ord('A') + remain - 10)
    return deverse(quotient, b) + remain_char

print(deverse(n,b))