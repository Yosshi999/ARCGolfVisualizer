f=lambda x:0<=x<21
def d(i,j,u,v,g):
 I=i;J=j
 c=0
 for p in range(3):
  for q in range(3):
   if f(I+u+p)and f(J+v+q)and g[I+u+p][J+v+q]:c=g[I+u+p][J+v+q]
 for k in range(5):
  I+=u;J+=v
  for p in range(3):
   for q in range(3):
    if f(I+p)and f(J+q):g[I+p][J+q]=c*(g[i+p][j+q]>0)
def p(g):
 a=[]
 for i in range(19):
  for j in range(19):
   a.append(sum([v>0for u in g[i:i+3] for v in u[j:j+3]]))
 X=a.index(max(a))
 i,j=X//19,X%19
 for x in [-4,0,4]:
  for y in [-4,0,4]:
   if x==y==0:continue 
   d(i,j,x,y,g)
 return g