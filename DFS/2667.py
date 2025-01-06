def dfs(graph, R, visited, cnt):
    stack = [R] 
    if visited[R]:
        return
    order = 1 
    while stack:
        node = stack.pop()
        if not visited[node]: 
            visited[node] = True 
            cnt += 1
            order += 1

            for neighbor in sorted(graph[node]):
                if not visited[neighbor]:
                    stack.append(neighbor)
    answer.append(cnt)

if __name__ == "__main__":    
    N = M= int(input())
    pointlist = []
    graph = [[] for _ in range(N**2)] 
    nodes = []
    for i in range(N):
        datas = [int(char) for char in input()]
        pointlist.append(datas)
        for j in range(N):
            y, x = i, j
            point = (x,y)
            if pointlist[y][x] == 1:
                nodes.append(x+y*N)
                if x!=0 and pointlist[y][x-1] and pointlist[y][x-1] == 1: #왼
                    if not (x-1+y*N) in graph[x+y*N]:
                        graph[x+y*N].append(x-1+y*N)
                        graph[x-1+y*N].append(x+y*N)
                if x!=N-1 and pointlist[y][x+1] and pointlist[y][x+1] == 1: #오
                    if not (x+1+y*N) in graph[x+y*N]:
                        graph[x+y*N].append(x+1+y*N)
                        graph[x+1+y*N].append(x+y*N)
                if y!=0 and pointlist[y-1][x] and pointlist[y-1][x] == 1: #위
                    if not (x+(y-1)*N) in graph[x+y*N]:
                        graph[x+y*N].append(x+(y-1)*N)
                        graph[x+(y-1)*N].append(x+y*N)

    visited = [False] * (N**2)
    answer = []
    for R in nodes:
        cnt = 0
        dfs(graph, R, visited, cnt)
    answer.sort()
    print(len(answer))
    print("\n".join(map(str, answer)))