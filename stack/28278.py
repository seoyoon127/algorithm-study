n = int(input())
inputList = []
for i in range (n):
    s = input()
    inputList.append(s)
stack = []

for i in inputList:
    if i[0]=="1":
        stack.append(i.split()[1])
    elif i=="2":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif i=="3":
        print(len(stack))
    elif i=="4":
        if stack:
            print(0)
        else:
            print(1)
    elif i=="5":
        if stack:
            print(stack[-1])
        else:
            print(-1)