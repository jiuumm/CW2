a=input()#중위식
stack=[]
res='' #여기에 출력하겠다.
for x in a:
    if x.isdecimal():
        res+=x
    else:
        if x=='(':
            stack.append('(')
        elif x=='*' or x=='/':
            #꺼내야 하는 순간(우선순위 높은 연산자가 있을 때)
            while stack and (stack[-1]=='*' and stack[-1]=='/'):
                res+=stack.pop()
            stack.append(x)
        elif x=='+'or x=='-':
            #꺼내야 하는 순간
            while stack and stack[-1] !='(':
                res+=stack.pop()
            #여는 괄호라면 덧셈연산자를 append해야함
            stack.append(x)
        elif x==')':
            while stack and stack[-1] !='(':
                res+=stack.pop()
            stack.pop()
while stack:
    res+=stack.pop()
print(res)