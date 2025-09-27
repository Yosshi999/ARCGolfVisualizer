r=range
m=[-4,0,4]
def p(g):
 _,i,j=max((sum(v>0for u in g[i:i+3]for v in u[j:j+3]),i,j)for i in r(19)for j in r(19))
 for x in m:
  for y in m:
   I=i;J=j;c=max(g[i+x+q//3][j+y+q%3]for q in r(9))
   for k in r(27):
    if(q:=k%9)<1:I+=x;J+=y
    if 21>I+q//3>-1<J+q%3<21:g[I+q//3][J+q%3]=c*(g[i+q//3][j+q%3]>0)
 return g