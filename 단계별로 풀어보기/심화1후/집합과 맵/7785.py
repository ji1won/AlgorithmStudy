n = int(input())
people = {}
for _ in range(n):
    name, enter = map(str,input().split())
    if enter == 'enter':
        people[name] = True
    else:
        people.pop(name)
for name in sorted(people.keys(),reverse=True):
    print(name)