r=range
def p(g):
 _,i,j=min((sum(u[j:j+3].count(0)for u in g[i:i+3]),i,j)for i in r(19)for j in r(19))
 for z in r(9):
  x=z//3*4-4;y=z%3*4-4;c=max(g[i+x+q//3][j+y+q%3]for q in r(9))
  for k in r(27):
   if 21>(I:=i+k//3%3+k//9*x+x)>-1<(J:=j+k%3+k//9*y+y)<21:g[I][J]=c*(g[i+k//3%3][j+k%3]>0)
 return g