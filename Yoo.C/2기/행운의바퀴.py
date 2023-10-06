#from collections import deque
n, k= map(int, input().split())
wheel = [0]*n
cnt=-1
flag=0
flag2 = True
for i in range(k):
    s, letter = map(str, input().split())
    s= int(s)
    cnt+=s
    if cnt>=n:
        cnt-=n
    if cnt==-1:
        flag2 = False
        break
  
    if wheel[cnt] == 0 or wheel[cnt]==letter:
        wheel[cnt]= letter
    else:
        print("!")
        flag2 = False
        break
    
    if i==k-1:
        flag = cnt
if flag2:
    left=[]
    right=[]
    for i in range(0, flag+1):
        if wheel[i]== 0:
            wheel[i]="?"
        left.append(wheel[i])
    for i in range(flag+1, len(wheel)):
        if wheel[i]==0:
            wheel[i]="?"
        right.append(wheel[i])

    while left:
        print(left.pop(), end="")
    while right:
        print(right.pop(), end="")