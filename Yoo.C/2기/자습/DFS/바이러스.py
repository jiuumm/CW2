
def dfs(x):
    global answer
    visited[x]=True
    answer+=1
    for node in graph[x]:
        if visited[node]:
            continue
        else:
            dfs(node)
if __name__=='__main__':
        #컴퓨터의 수
    v=int(input())
    e = int(input())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    answer=0
    visited = [False for _ in range(v+1)]
    dfs(1)
    print(answer-1)