
n=int(input())#5
a=input()#ABC*+DE/-
num= [int(input()) for i in range(n)]#1 2 3 4 5

stack=[]
res=0
for x in a:
    if x.isalpha():
        stack.append(num[ord(x)-65])
    elif stack and x=='*':
        res=stack.pop()*stack.pop()
        stack.append(res)
        # print(stack)
    elif stack and x=='/':
        m= stack.pop()
        n= stack.pop()
        res=n/m
        stack.append(res)
    elif stack and x=='+':
        res=stack.pop()+stack.pop()
        stack.append(res)

    elif stack and x=='-':
        m=stack.pop()
        n= stack.pop()
        res=n-m
        stack.append(res)
if stack:
    print('%.2f' %res)

        
        