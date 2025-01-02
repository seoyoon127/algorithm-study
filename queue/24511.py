import sys
from collections import deque
ins = sys.stdin.read().splitlines()
n = int(ins[0])
queuestack = list(map(int, ins[1].split()))
lists = list(map(int, ins[2].split()))
m = int(ins[3])
inputs = list(map(int, ins[4].split()))

queue = deque()
answer=[]

for i in range(n):
    if queuestack[i]==0:
        queue.append(lists[i])

for i in inputs:
        queue.appendleft(i)
        answer.append(queue.pop())
print(" ".join(map(str,answer)))