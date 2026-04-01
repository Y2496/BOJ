import sys

# 파이썬의 기본 재귀 한도는 1000입니다. 
# 이 문제처럼 노드 수가 많을 때는 재귀 한도를 반드시 늘려주어야 'RecursionError'가 발생하지 않습니다.
sys.setrecursionlimit(10**6)

# 입력을 빠르게 받기 위해 sys.stdin.readline을 사용합니다.
input = sys.stdin.readline

def solve():
    # 1. 입력 받기 (N: 정점의 수, M: 간선의 수, R: 시작 정점)
    n, m, r = map(int, input().split())
    
    # 2. 인접 리스트로 그래프 구현하기
    # 각 정점마다 연결된 노드들을 담을 리스트를 만듭니다 (1번부터 N번까지 사용).
    graph = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u) # 무방향 그래프이므로 양쪽 모두 추가
        
    # 3. 오름차순 방문을 위해 각 인접 리스트 정렬하기
    # 문제에서 '인접 정점은 오름차순으로 방문한다'고 명시되어 있습니다.
    for i in range(1, n + 1):
        graph[i].sort()
        
    # 4. 방문 순서를 기록할 리스트와 카운트 변수 준비
    # visited[i]는 i번 노드가 몇 번째로 방문되었는지를 저장합니다 (0이면 미방문).
    visited = [0] * (n + 1)
    count = 1 # 방문 순서를 매길 변수

    # 5. DFS 함수 정의
    def dfs(curr_node):
        nonlocal count # 바깥쪽의 count 변수를 사용하겠다고 선언
        
        # 현재 노드 방문 처리 (현재의 순서를 기록하고 다음 순번을 위해 1 증가)
        visited[curr_node] = count
        count += 1
        
        # 연결된 노드들을 하나씩 확인
        for next_node in graph[curr_node]:
            # 아직 방문하지 않은 노드라면 재귀적으로 탐색 진행
            if visited[next_node] == 0:
                dfs(next_node)

    # 6. 시작 정점 R에서 DFS 탐색 시작
    dfs(r)

    # 7. 결과 출력 (1번 정점부터 N번 정점까지 방문 순서를 한 줄씩 출력)
    for i in range(1, n + 1):
        print(visited[i])

# 프로그램 실행
if __name__ == "__main__":
    solve()