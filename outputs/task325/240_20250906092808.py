R=range
def p(g):
 H=len(g);W=len(g[0]);G=sum(g,[])
 D=lambda z:H*W>z>=0<(c:=G[z])and sum((D(z+a)for a in[-1,-W,-~z%W>0,W][z%W<1:G.__setitem__(z,0)]),1)
 n=sum([D(i)>0for i in R(H*W)])
 print(n)
 return[[8*(y==x)for x in R(n)]for y in R(n)]