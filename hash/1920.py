N = int(input())
A = list(map(int, input().split())) 
M = int(input())
X = list(map(int, input().split())) 
for x in X:
    print(1 if x in A else 0)