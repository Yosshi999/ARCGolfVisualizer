f=lambda x:0<=x<21
r=range
m=[-4,0,4]
def p(g):
 _,i,j=max((sum(v>0for u in g[i:i+3]for v in u[j:j+3]),i,j)for i in r(19)for j in r(19))
 for x in m:
  for y in m:
   I=i;J=j;c=max(g[i+x+q//3][j+y+q%3]for q in r(9))
   for k in r(45):
    if(q:=k%9)<1:I+=x;J+=y
    if f(X:=I+q//3)*f(Y:=J+q%3):g[X][Y]=c*(g[i+q//3][j+q%3]>0)
 return g