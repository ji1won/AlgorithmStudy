n = int(input())
index = 3

def circle(n):
    global index
    if n == 1:
        return index
    else:
        index = index * 2 - 1
        return circle(n - 1)

result = circle(n)
print(result**2)