import sys
from queue import PriorityQueue

input = sys.stdin.readline
N = int(input()) 
minusNum = PriorityQueue() 
plusNum = PriorityQueue()
zeroCnt, oneCnt = 0, 0

#데이터 분리 저장
for _ in range(N):
    x = int(input())
    if x == 0:
        zeroCnt += 1
    elif x == 1:
        oneCnt += 1
    elif x < 0:
        minusNum.put(x)
    else:
        plusNum.put(-x)

answer = 0

#양수 처리
while plusNum.qsize() > 1:
    a = plusNum.get() *-1
    b = plusNum.get() *-1
    answer += a*b
if plusNum.qsize() > 0:
    answer += plusNum.get() *-1

#음수 처리
while minusNum.qsize() > 1:
    a = minusNum.get()
    b = minusNum.get()
    answer += a*b
if minusNum.qsize() > 0:
    if zeroCnt > 0:
        zeroCnt -= 1
    else:
        answer += minusNum.get()

answer += oneCnt
print(answer)