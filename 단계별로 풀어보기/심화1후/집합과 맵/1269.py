a_len, b_len = map(int, input().split())

a = set(map(int,input().split()))
b = set(map(int, input().split()))

a_b = set()
for A in a:
    if A not in b:
        a_b.add(A)

for B in b:
    if B not in a:
        a_b.add(B)
        
print(len(a_b))
