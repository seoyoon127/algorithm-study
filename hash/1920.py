import sys
input = sys.stdin.readline  # 한 줄씩 입력받기

N = int(input().strip())  # 첫 번째 입력: N
A = set(input().split())  # 두 번째 입력: A (set으로 변환)

M = int(input().strip())  # 세 번째 입력: M
X = input().split()  # 네 번째 입력: X 리스트

for x in X:
    print(1 if x in A else 0)
