N = int(input())
stack = []
answer = []
for i in range(N):
    x = input().split()
    if x[0] == "push":
        stack.append(x[1])
    elif x[0] == "pop":
        if len(stack) != 0:
            answer.append(stack.pop())
        else:
            answer.append(-1)
    elif x[0] == "size":
        answer.append((len(stack)))
    elif x[0] == "empty":
        answer.append(1 if len(stack)==0 else 0)
    elif x[0] == "top":
        if len(stack) != 0:
            answer.append(stack[-1])
        else:
            answer.append(-1)
for i in answer:
    print(i)