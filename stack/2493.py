N = int(input())
nums = list(map(int, input().split()))
stack = []
index = []
answer = []
for i in range(N):
    x = nums[i]
    while len(stack) > 0 and x > stack[-1][0]:
        stack.pop()
    answer.append(stack[-1][1]+1 if stack else 0)
    stack.append((x,i))

print(" ".join(map(str, answer)))