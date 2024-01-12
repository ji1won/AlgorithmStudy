n = int(input())
def dis (word):
    if len(word) >= 3:
        for i in range(len(word)):
            for j in range(i+2,len(word)):
                if word[j] == word[i]:
                    return True
    return False

count = 0
for _ in range(n):
    if dis(list(input())):
        count += 1
print(count)

