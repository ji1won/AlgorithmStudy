def gcd(a, b):
    # 최대공약수 계산
    while b:
        a, b = b, a % b
    return a

n = int(input())  # 가로수의 개수
positions = [int(input()) for _ in range(n)]  # 가로수의 위치

gaps = []  # 가로수 사이의 간격을 저장할 리스트

# 가로수 사이의 간격을 구해서 gaps 리스트에 저장
for i in range(1, n):
    gaps.append(positions[i] - positions[i-1])

# 가로수 사이의 간격들의 최대공약수 계산
gap_gcd = gaps[0]
for gap in gaps[1:]:
    gap_gcd = gcd(gap_gcd, gap)

# 추가로 심어야 할 가로수의 개수 계산
additional_trees = 0
for gap in gaps:
    additional_trees += gap // gap_gcd - 1

print(additional_trees)
