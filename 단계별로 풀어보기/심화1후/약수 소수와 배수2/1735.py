a, b = map(int,input().split())
c, d = map(int, input().split())

m = b*d
s = a*d + c*b

def lcd(s,m):
    while m:
        s,m = m, s%m
    return s

lcd = lcd(s,m)
print(s//lcd, m//lcd)