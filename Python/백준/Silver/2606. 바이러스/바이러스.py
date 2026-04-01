import sys
from collections import deque

input_fast = sys.stdin.readline

# 컴퓨터의 수(정점)와 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수(간선)
n = int(input_fast())
m = int(input_fast())

graph = [[] for _ in range(n + 1)]

# 네트워크 연결 정보 입력 (양방향)
for _ in range(m):
    a, b = map(int, input_fast().split())
    graph[a].append(b)
    graph[b].append(a)

# 바이러스 감염을 탐색할 BFS 함수
def bfs_virus(start):
    queue = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True
    count = 0 # 1번 컴퓨터를 통해 감염된 컴퓨터의 수
    
    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                count += 1 # 새로 방문할 때마다 감염된 컴퓨터 수 1 증가
                
    return count

# 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 감염되는 컴퓨터의 수 출력
print(bfs_virus(1))