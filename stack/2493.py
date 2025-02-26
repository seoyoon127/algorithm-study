N = int(input())
nums = list(map(int, input().split()))
answer = []
for i in range(N):
    x = nums.pop()
    prev = -1
    while -prev <= len(nums) and nums[prev] < x:
        prev -= 1
    if -prev > len(nums):
        answer.append(0)
    else:
        answer.append(N-i+prev)
print(" ".join(map(str, sorted(answer, reverse=True))))