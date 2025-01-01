import sys
from collections import deque
n=int(input())
answer=deque()
lists = sys.stdin.read().splitlines()  

for list in lists:
    list = list.split()
    if list[0] == '1':
        answer.appendleft(list[1])
    elif list[0] == '2':
        answer.append(list[1])
    elif list[0] == '3':
        print(answer.popleft() if answer else -1)
    elif list[0] == '4':
        print(answer.pop() if answer else -1)
    elif list[0] == '5':
        print(len(answer))
    elif list[0] == '6':
        print(1 if len(answer)==0 else 0)
    elif list[0] == '7':
        print(answer[0] if answer else -1)
    elif list[0] == '8':
        print(answer[-1] if answer else -1)