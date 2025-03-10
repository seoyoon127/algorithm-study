import sys
input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split())
arr = list(map(int, data[1].split()))
S = [0]
temp = 0

for i in arr:
    temp += i
    S.append(temp)

for i in range(M):
    left, right = map(int, data[i+2].split())
    print(S[right] - S[left-1]) 