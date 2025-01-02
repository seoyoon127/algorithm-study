string = list(input())
bomb = list(input())
stack = []

for i in string:
    stack.append(i)
    if i == bomb[-1]:
        if stack[-len(bomb):] == bomb:
            for i in range(len(bomb)):
                stack.pop()

print("".join(stack) if stack else 'FRULA')

#stack = stack[:-len(bomb)]