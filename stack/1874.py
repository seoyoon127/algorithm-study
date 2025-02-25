N = int(input())
stack = []
answer = []
next = 1

for i in range(N):
    x = int(input())
    print(x, stack)
    while next <= x:
        stack.append(next)
        answer.append("+")
        next += 1

    if stack[-1] == x:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        exit(0)

print("\n".join(answer))

# if len(stack) == 0:
#         next = x+1
#         for i in range(x):
#             stack.append(i+1)
#             answer.append('+')
#         stack.pop()
#         answer.append('-')
#     elif x == stack[-1]:
#         stack.pop()
#         answer.append('-')
#     elif x > stack[-1]:
#         if x >= next:
#             for i in range(next, x+1):
#                 answer.append('+')
#                 stack.append(i)
#             next = x+1
#             stack.pop()
#             answer.append('-')
#     elif x < stack[-1]:
#         print("NO")
#         exit(0)