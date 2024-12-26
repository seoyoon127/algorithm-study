import sys

def Max_heap(A, root, n):
    largest = root
    left = root*2+1
    right = root*2+2
    if left < n and A[left] > A[largest]:
        largest = left
    if right < n and A[right] > A[largest]:
        largest = right
    if largest != root:
        A[root], A[largest] = A[largest], A[root]
        Max_heap(A, largest, n)

def heap_sort(A):
    n = len(A)
    # 힙 생성
    for i in range(n // 2 - 1, -1, -1):
        Max_heap(A, i, n)
    # 정렬 수행
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        Max_heap(A, 0, i)

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split('/n')
    n = int(data[0])
    A = list(map(int, data[1:]))
    
    heap_sort(A)

    for i in A:
        print(i)