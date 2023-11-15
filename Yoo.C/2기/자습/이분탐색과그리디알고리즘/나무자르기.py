n, m= map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
lt=1
rt=lst[-1]
res=0
def Count(mid):
    sm=0
    for x in lst:
        if x>mid:
            sm+=(x-mid)
        else:
            continue
    return sm
    
while lt<=rt:
    mid = (lt+rt)//2
    sm=0

    if Count(mid)>=m:#m을 여기다가 포함시켜야함!
        #높이를 작게잡음
        lt=mid+1
        
    elif Count(mid)<m:# 높이를 너무 크게 잡음
        rt=mid-1
        res=mid#여기 놓침
        
                
print(rt)