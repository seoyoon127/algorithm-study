# n=int(input())
# balloonNum = [i+1 for i in range (n)]
# numList=list(map(int,input().split()))
# s = 0
# answer=[]
# while balloonNum:
#     answer.append(balloonNum.pop(s))
#     if len(balloonNum) == 0:
#         s=0
#     elif numList[s]>0:
#         s=(s+(numList.pop(s)%len(balloonNum))-1)%len(balloonNum)
#     elif numList[s]<=0:
#         s=(s+(numList.pop(s)%len(balloonNum)))%len(balloonNum)
# print(" ".join(map(str, answer)))

from collections import deque

N = int(input())
M = list(map(int, input().split()))
que = deque((i+1,M[i]) for i in range (len(M)))

answer = []

while que:
    turn, number = que.popleft()
    answer.append(turn)

    if que and number > 0:
        number = number % len(que) -1
        
    que.rotate(-number)

print(*answer)