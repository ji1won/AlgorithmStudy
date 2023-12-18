n = int(input())
stackList = []

for i in range (n):
    command = input().split()
    order = str(command[0])
   
    if order == 'push':
        num = int(command[1])
        stackList.append(num)
        
    elif order == 'pop':
        if len(stackList) != 0:
            pop = stackList.pop()
            print(pop)
        else :
            print(-1)
    elif order == 'size':
        print(len(stackList))
    elif order == 'top':
        if len(stackList) != 0:
            print(stackList[-1])
        else :
            print(-1)
    elif order == 'empty':
        if len(stackList) == 0:
            print(1)
        else :
            print(0)
        
    