import sys
input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split())
arr = list(map(int, data[1].split()))

for i in range(M):
    left, right = map(int, data[i+2].split())
    print(sum(arr[left-1:right])) 