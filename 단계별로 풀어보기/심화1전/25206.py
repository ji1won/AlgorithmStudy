count = 0.0
result = 0.0
def cal (g, s):
    global count, result
    if s == 'A+':
        result += g*4.5
        count += g
    elif s == 'A0':
        result += g*4.0
        count += g
    elif s == 'B+':
        result += g*3.5
        count += g
    elif s == 'B0':
        result += g*3.0
        count += g
    elif s == 'C+':
        result += g*2.5
        count += g
    elif s == 'C0':
        result += g*2.0
        count += g
    elif s == 'D+':
        result += g*1.5
        count += g
    elif s == 'D0':
        result += g*1.0
        count += g
    elif s == 'F':
        result += g*0.0
        count += g

    

for _ in range(20):
    subject, grade, score = input().split()
    grade = float(grade)
    if score != 'P':
        cal(grade, score)

if count != 0:print(round(result / count,6))
else: print(0.000000)