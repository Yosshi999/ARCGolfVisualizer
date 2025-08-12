def p(q):
 C=0;G=[];H=[]
 g=[[0]*12for _ in range(12)]
 for i in range(10):
  for j in range(10):g[i+1][j+1]=q[i][j]
 for i in range(10):
  for j in range(10):
   S={v for u in g[i:i+3]for v in u[j:j+3]}
   if len(S)==2:
    c=list(S-{0})[0]
    if C>0and C!=c:H+=[[v[j:j+3]for v in g[i:i+3]]]
    else:
     C=c;G+=[[v[j:j+3]for v in g[i:i+3]]]
 for u in G:
  for v in H:
   w=[[u[i][j]or v[i][j] for j in range(3)]for i in range(3)]
   if all(x>0for r in w for x in r):return w