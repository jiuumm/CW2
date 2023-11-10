n, k=map(int, input().split())
#어떤수 n이 1이 될떄까지! k로 나눠지면 나눈다.
cnt=0

def dfs(n, cnt):
    if n==1:
        print(cnt)
        return

    
    if n%k==0:
        cnt+=1
        dfs(n//k, cnt)
    else:
        cnt+=1
        dfs(n-1, cnt)

dfs(n, cnt)