import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
heights = list(map(int, data[1:]))
stack = []
answer = 0

for i in range(N):
    x = heights.pop()
    while stack and stack[-1][0] < x:
        stack.pop()
    answer += stack[-1][1]-N+i-1 if stack else i
    stack.append((x, N-i))
print(answer)

#반례: 오큰수가 없는 경우