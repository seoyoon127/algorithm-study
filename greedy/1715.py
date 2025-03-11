import sys
from queue import PriorityQueue

input = sys.stdin.readline

N = int(input()) 
cards = PriorityQueue()  # 우선순위 큐 생성

# 입력값을 우선순위 큐에 넣기
for _ in range(N):
    cards.put(int(input()))

total_sum = 0  # 총 비용 저장

# 카드 합치기 (최소 비용으로)
while cards.qsize() > 1:  # 2개 이상 남아 있어야 합칠 수 있음
    a = cards.get()  # 가장 작은 값
    b = cards.get()  # 두 번째로 작은 값
    cost = a + b  # 두 카드 묶기 비용
    total_sum += cost  # 총 비용에 추가
    cards.put(cost)  # 묶은 카드 다시 큐에 넣기

print(total_sum)  # 최종 결과 출력
