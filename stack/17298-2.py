N = int(input())
nums = list(map(int, input().split()))
stack = []
answer = []

for i in range(N-1,-1,-1):
    x = nums[i]
    while stack and stack[-1] <= x:
        stack.pop()
    answer.append(stack[-1] if stack else -1)
    stack.append(x)
print(" ".join(map(str, answer[::-1])))