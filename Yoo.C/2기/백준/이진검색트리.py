import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def solution(tree):
    if len(tree)==0:
        return
    tmpL, tmpR= [], []
    #첫번째 값= 루트 노드
    root = tree[0]
    for i in range(1, len(tree)):
        if tree[i]> root:
            #루트노드보다 작은 값들
            tmpL = tree[1:i]
            tmpR = tree[i:]
            break
    else:
        tmpL = tree[1:]
       
    solution(tmpL)
    solution(tmpR)
    print(root)
    
if __name__=='__main__':
    tree=[]
    while True:
        try:
            tree.append(int(input()))
        except:
            break
    solution(tree)    