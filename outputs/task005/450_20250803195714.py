f=lambda x:0<=x<21
r=range
def d(i,j,u,v,g):
 I,J,c=i,j,0
 for p in r(9): 
  if f(s:=I+u+p//3)and f(t:=J+v+p%3)and (m:=g[s][t]):c=m
 for k in r(45):
  if (p:=k%9)==0:I+=u;J+=v
  if f(I+p//3)and f(J+p%3):g[I+p//3][J+p%3]=c*(g[i+p//3][j+p%3]>0)
def p(g):
 a=[]
 for i in r(361):
  a+=[sum([v>0for u in g[i//19:i//19+3] for v in u[i%19:i%19+3]])];X=a.index(max(a))
 i,j=X//19,X%19;m=[-4,0,4];[d(i,j,x,y,g)if x*3-y else 0 for y in m for x in m]
 return g