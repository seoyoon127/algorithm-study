def dfs(graph, R, visited, answer):
    stack = [R]  # 탐색 시작 노드를 스택에 추가
    order = 1    # 방문 순서

    while stack:
        node = stack.pop()
        if not visited[node]:  # 방문하지 않은 경우에만 처리
            visited[node] = True  # 방문 처리
            answer[node] = order  # 방문 순서 저장
            order += 1

            # 현재 노드에 연결된 노드를 스택에 추가
            for neighbor in sorted(graph[node]):
                if not visited[neighbor]:
                    stack.append(neighbor)

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    # 첫 번째 줄: N(노드 수), M(간선 수), R(시작 노드)
    N, M, R = map(int, data[0].split())
    
    # 그래프 입력
    graph = [[] for _ in range(N + 1)]  # 인접 리스트
    for i in range(1, M + 1):
        u, v = map(int, data[i].split())
        graph[u].append(v)
        graph[v].append(u)
    visited = [False] * (N + 1)
    answer = [0] * (N + 1)
    dfs(graph, R, visited, answer)
    print("\n".join(map(str, answer[1:]))) 
