import sys
sys.setrecursionlimit(10000)

def dfs(y, x, graph):
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    graph[y][x] = 0  # 방문 처리
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
            dfs(ny, nx, graph)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        m, n, k = map(int, input().split())
        graph = [[0] * m for _ in range(n)]
        for _ in range(k):
            x, y = map(int, input().split())
            graph[y][x] = 1

        count = 0  # 연결된 구성 요소 수
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 1:  # 1이면 DFS 탐색 시작
                    dfs(i, j, graph)
                    count += 1  # 연결된 구성 요소 수 증가
        print(count)
