a,b = map(int, input().split())
def gcd(a,b):
    while b:
        a, b = b, a%b
    return a
def lcd(a,b):
    return a*b // gcd(a,b)

print(lcd(a,b))