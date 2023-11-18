n, m =map(int, input().split())
music = list(map(int, input().split()))

lt=1
rt=sum(music)
res=0

def Count(capacity):
    cnt=1
    sum=0
    for x in music:
        if sum+x>capacity:
            cnt+=1
            sum=x
        else:
            sum+=x
    return cnt

while lt<rt:
    mid=(lt+rt)//2
    if Count(mid)<=m:
        res = mid
        rt=mid-1
    else:
        lt=mid+1