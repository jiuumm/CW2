import sys
sys.setrecursionlimit(10**6)
num_list = []
while True:
    try:
        num = int(input())
        num_list.append(num)
    except:
        break

def postorder(first,end):
    if first > end:
        return
    mid = end+1   # 루트보다 큰 값이 존재하지 않을 경우를 대비   
    for i in range(first+1,end+1):
        if num_list[first] < num_list[i]:
            mid = i
            break
    
    postorder(first+1, mid-1)
    postorder(mid, end)
    print(num_list[first])

postorder(0,len(num_list)-1)


//루트 값을 기준으로 루트보다 큰 값이 존재하면 그 값을 기준으로 왼쪽, 오른쪽 트리를 나눠주었다. 재귀를 통해 이 과정을 계속 반복하면 왼쪽 서브트리 - 오른쪽 서브트리 - 루트 순서대로 출력이 된다.