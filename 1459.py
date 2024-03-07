x, y, w, s = map(int, input().split())
#평행이동
m1 = (x+y)*w

#대각선이동
if (x+y)%2 == 0:
    m2 = max(x,y)*s
#대각선에 직선 한번(홀수)
else:
    m2 = (max(x,y)-1)*s + w

#섞어서
m3 = min(x,y)*s + abs(x-y)*w

print(min(m1, m2, m3))