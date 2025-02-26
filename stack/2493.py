N = int(input())
nums = list(map(int, input().split()))
nums2 = []
answer = []
answer2 = []
for i in range(int(N/2)+1):
    x = nums.pop()
    if len(nums) >= i+1:
        nums2.append(nums[i])
    if len(nums2) >= i+1:
        if nums2[i] == max(nums2):
            answer2.append(0)
        else:
            answer2.append(nums.index(max(nums2)))
    prev = -1
    while -prev <= len(nums) and nums[prev] < x:
        prev -= 1
    if -prev > len(nums):
        answer.append(0)
    else:
        answer.append(N-i+prev) 
print(" ".join(map(str, sorted(answer2+answer)))) 