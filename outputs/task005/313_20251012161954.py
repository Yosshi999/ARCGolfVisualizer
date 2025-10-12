r=range
def p(g):
 _,i,j=min((sum(u[j:j+3].count(0)for u in g[i:i+3]),i,j)for i in r(19)for j in r(19))
 for z in r(9):
  x=z//3*4-4;y=z%3*4-4;I=i;J=j;c=max(g[i+x+q//3][j+y+q%3]for q in r(9))
  for k in r(27):
   if(q:=k%9)<1:I+=x;J+=y
   if 21>I+q//3>-1<J+q%3<21:g[I+q//3][J+q%3]=c*(g[i+q//3][j+q%3]>0)
 return g