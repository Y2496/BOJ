import sys
from collections import deque

input_fast = sys.stdin.readline

# N: 정점 수, M: 간선 수, R: 시작 정점
N, M, R = map(int, input_fast().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input_fast().split())
    graph[u].append(v)
    graph[v].append(u)

# "인접 정점은 오름차순으로 방문한다"는 조건이 있으므로 정렬 필수
for i in range(1, N + 1):
    graph[i].sort()

# 방문 순서를 기록할 배열 (0으로 초기화, 0이면 아직 방문 안 했다는 뜻)
visited_order = [0] * (N + 1)

def bfs_order(start):
    queue = deque([start])
    order = 1 # 방문 순서 카운터 (시작 정점이 1번째)
    visited_order[start] = order
    
    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            if visited_order[i] == 0: # 아직 방문하지 않은 노드라면
                order += 1            # 방문 순서를 1 증가시키고
                visited_order[i] = order # 해당 정점에 방문 순서를 기록함
                queue.append(i)

# BFS 실행 (R번 정점에서 시작)
bfs_order(R)

# 1번 정점부터 N번 정점까지 방문 순서를 차례대로 출력
for i in range(1, N + 1):
    print(visited_order[i])