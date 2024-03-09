import sys
a,b = map(int, sys.stdin.readline().split())
c =int(input())

c_h, c_m = divmod(c,60)
r_h, r_m = a+c_h, b+c_m

if r_m>59:
    r_h += 1
    r_m -= 60
if r_h >23:
    r_h -= 24
    print(r_h ,r_m)
else:
    print(r_h, r_m)
