import math
N,M = map(int, input().split())
if N ==1: N =2
arr=[0] * (M+1)
for i in range(N, M+1):
    arr[i] = i

for i in arr:
    if arr[i] != 0:
        for j in range(2, int(math.sqrt(i))+1):
            if i%j == 0:
                arr[i] = 0
                break

for i in range(len(arr)):
    if arr[i] != 0:
        print(i)