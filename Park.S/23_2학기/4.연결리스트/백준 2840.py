#231006(FRI) / 연결 리스트 / 실버4
#돌림판을 돌리자.... 
#덱으로 구현
#예외처리;;;; 


from collections import deque

def isPossible(re, temp):
    if re != '?' and re != temp:
        possible[0] = False
        return False
    return True

def input(re, temp):
    try:
        count[temp] += 1
        if re != temp:
            possible[0] = False
        else:
            wheel.appendleft(temp)
    except:
        count[temp] = 1
        wheel.appendleft(temp)

def result():
    if possible[0]:
        print(wheel.popleft(), end="")
        while wheel:
            print(wheel.pop(), end="")
    else:
        print("!")

if __name__ == '__main__':
    N, K = map(int, input().split())
    wheel = deque(['?'] * N)
    count = dict()
    possible = [True]
    
    for _ in range(K):
        n, temp = map(str, input().split())
        n = int(n)
        
        for i in range(n):
            wheel.append(wheel.popleft())
            
        currentChar = wheel.popleft()
        
        if not isPossible(currentChar, temp):
            break
        
        input(currentChar, temp)
    
    result()
