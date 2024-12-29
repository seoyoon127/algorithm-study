import sys
from collections import deque

n = int(input())  # 큐 연산의 수
queue = deque()
answer = []

# 한 번에 입력 받기
input = sys.stdin.read

# 각 연산을 처리
for line in input().splitlines():
    input_data = line.split()
    if input_data[0] == 'push':
        queue.append(input_data[1])
    elif input_data[0] == 'pop':
        x = queue.popleft() if queue else -1
        answer.append(str(x))
    elif input_data[0] == 'size':
        answer.append(str(len(queue)))
    elif input_data[0] == 'empty':
        x = 1 if not queue else 0
        answer.append(str(x))
    elif input_data[0] == 'front':
        x = queue[0] if queue else -1
        answer.append(str(x))
    elif input_data[0] == 'back':
        x = queue[-1] if queue else -1
        answer.append(str(x))

# 한 번에 출력하기
sys.stdout.write("\n".join(answer) + "\n")
