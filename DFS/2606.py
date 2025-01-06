def dfs(graph, R, visited):
    stack = [R] 

    while stack:
        node = stack.pop()
        if not visited[node]:  
            visited[node] = True 

            for neighbor in sorted(graph[node]):
                if not visited[neighbor]:
                    stack.append(neighbor)

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    # N(노드 수), M(간선 수), R(시작 노드)
    N, M, R = int(data[0]), int(data[1]), 1
    
    # 그래프 입력
    graph = [[] for _ in range(N+1)]  # 인접 리스트
    for i in range(2, M + 2):
        u, v = map(int, data[i].split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (N + 1)
    dfs(graph, R, visited)
    print(visited.count(True)-1) 