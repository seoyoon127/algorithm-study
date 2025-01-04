n = int(input())
nums = list(map(int,input().split()))
stack = []
answer = []

while len(nums)>0:
    tmp = nums.pop()
    if len(stack)==0:
        stack.append(tmp)
        answer.append(-1)
    else:
        if tmp >= stack[-1]:
            while len(stack) and stack[-1] <= tmp:
                stack.pop()
        if len(stack)==0:
            answer.append(-1)
        else:
            answer.append(stack[-1])
        stack.append(tmp)

for i in range(len(answer)-1, -1, -1):
    print(answer[i], end=' ')