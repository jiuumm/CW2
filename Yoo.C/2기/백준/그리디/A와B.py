
s=input()
t=input()
lst=[]
def dfs(s):
    if len(s)==len(t):    
        if s==t:
            lst.append("1")   
            return
        else:
            return
    if len(s)>len(t):
        return
    else:
        dfs(s+"A")
        dfs(s[::-1]+"B")
    
dfs(s)   
if "1" in lst:
    print("1")
else:
    print("0")