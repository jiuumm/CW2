a=input()#중위식
stack=[]
res='' #여기에 출력하겠다.
for x in a:
    if x.isalpha():
        res+=x
    else:
        if x=="(":
            stack.append('(')
        elif x=='*' or x=='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                res+=stack.pop()
            stack.append(x)
        elif x=='+' or x=='-':
            while stack and (stack[-1] !='('):
                res+=stack.pop()
            stack.append(x)
        elif x==')':
            while stack and (stack[-1] !='('):
                res+=stack.pop()
            stack.pop()#여는 괄호 닫기
while stack:
    res+=stack.pop()
            
print(res)




                
        