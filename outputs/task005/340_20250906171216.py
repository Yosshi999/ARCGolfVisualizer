f=lambda x:0<=x<21
r=range
m=[-4,0,4]
def p(g):
 _,i,j=max((sum(v>0for u in g[k//19:][:3]for v in u[k%19:][:3]),k//19,k%19)for k in r(361))
 for x in m:
  for y in m:
   I=i;J=j;c=max(g[i+x+q//3][j+y+q%3]for q in r(9))
   for k in r(45):
    if(q:=k%9)<1:I+=x;J+=y
    if f(I+q//3)*f(J+q%3):g[I+q//3][J+q%3]=c*(g[i+q//3][j+q%3]>0)
 return g