t = int(input())
def gcd(a,b): #최대공약수
    while b:
        a,b = b, a%b
    return a

def lcd(a,b): #최소공배수
    return (a*b)//gcd(a,b)

for _ in range(t):
    a,b = map(int, input().split())
    print(lcd(a,b))