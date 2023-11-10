from queue import PriorityQueue



'''
        1
    4       3
        10     5
'''
que = PriorityQueue(maxsize=8)
que.put((3, 'Apple'))
que.put((2, 'Orange'))
que.put((5, 'strawberry'))
print(que.get())
'''


'''
# import heapq
# n= int(input())
# hq=[]
# for i in range(n):
#     tmp= int(input())
#     if tmp==0:
#         if len(hq)==0:
#             print(0)
#         else:
#             print(heapq.heappop(hq))
#     else:
#         heapq.heappush(hq, tmp)
        
import heapq
n= int(input())
hq=[]
for i in range(n):
    tmp = int(input())
    heapq.heappush(hq,(-tmp, tmp))
    #홀수개라면
    if len(hq) %2 !=0:
        idx = len(hq)//2
        print(heapq.heappop(hq)[idx])
        
    #짝수개라면 
    else:
        idx1 = len(hq)//2-1
        idx2 = len(hq)//2
        print(min(heapq.heappop(hq)[idx1], heapq.heappop(hq)[idx2]))
    