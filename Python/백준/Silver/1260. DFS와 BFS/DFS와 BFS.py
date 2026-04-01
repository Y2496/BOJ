import sys
from collections import deque

input_fast = sys.stdin.readline

def dfs(graph, v, visited):
    # 1. 현재 노드를 방문 처리하고 화면에 출력합니다.
    visited[v] = True
    print(v, end=' ')
    
    # 2. 현재 노드와 연결된 다른 노드들을 재귀적으로 방문합니다.
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    # 1. 시작 노드를 큐(Queue)에 넣고 방문 처리합니다.
    queue = deque([start])
    visited[start] = True
    
    # 2. 큐가 빌 때까지 반복합니다.
    while queue:
        # 3. 큐에서 하나의 원소를 뽑아 출력합니다.
        v = queue.popleft()
        print(v, end=' ')
        
        # 4. 해당 원소와 연결된, 아직 방문하지 않은 노드들을 큐에 삽입합니다.
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# N: 정점의 개수, M: 간선의 개수, V: 탐색을 시작할 정점 번호
N, M, V = map(int, input_fast().split())

# 그래프 초기화 (1번부터 N번까지의 인덱스를 사용하기 위해 N+1 크기로 생성)
graph = [[] for _ in range(N + 1)]

# 간선 정보 입력받기 (양방향 그래프)
for _ in range(M):
    a, b = map(int, input_fast().split())
    graph[a].append(b)
    graph[b].append(a)

# 작은 번호의 정점부터 방문하기 위해 각 리스트를 오름차순 정렬
for i in range(1, N + 1):
    graph[i].sort()

# DFS 실행
visited_dfs = [False] * (N + 1)
dfs(graph, V, visited_dfs)
print() # 줄바꿈

# BFS 실행
visited_bfs = [False] * (N + 1)
bfs(graph, V, visited_bfs)