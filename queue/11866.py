from collections import deque
inputs = list(map(int,input().split()))
list = deque(i+1 for i in range(inputs[0]))
jump = inputs[1]
answer=[]
print('f',list)
while list:
    list.rotate(len(list)-jump+1)
    answer.append(list.popleft())
print("<"+", ".join(map(str,answer))+">")