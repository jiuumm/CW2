x=input()
if '0' not in x:
    print(-1)
else:
    sm=0
    for i in range(len(x)):
        sm+=int(x[i])
    if sm %3 !=0:
        print(-1)
        
    else:
        sorted_num = sorted(x, reverse=True)
        answer = ''
        for i in sorted_num:
            answer+=i
        print(answer)
    