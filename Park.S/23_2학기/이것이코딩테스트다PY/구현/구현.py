#구현 : 머릿속에 있는 알고리즘을 정확하고 빠르게 프로그램으로 작성하기
#4-1 상하좌우(시뮬레이션)

n = int(input())
x,y = 1,1
plans= input().split()

#L,R,U,D에 따른 이동방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = {'L','R','U','D'}

#이동계획 하나씩 확인
for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x+dx[i]
            ny = y+dy[i]
    
    #공간 벗어나면 무시
    if nx<1 or ny<1 or nx>n or ny>n:
        continue

    x,y = nx, ny

print(x,y)

#4-2 시각


