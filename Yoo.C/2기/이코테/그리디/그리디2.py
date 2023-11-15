n,m,k= map(int, input().split())
lst= list(map(int, input().split()))
lst.sort(reverse=True)
#숫자가 더해지는 총 횟수:m
#한 숫자가 연속적으로 k번을 초과하여 더해질 수 없다.
cnt=k
answer=0

while True:
    for i in range(k):
        if m==0:
            break
        answer+=lst[0]
        m-=1
    if m==0:
        break
    answer+=lst[1]
    m-=1
print(answer)
    
    