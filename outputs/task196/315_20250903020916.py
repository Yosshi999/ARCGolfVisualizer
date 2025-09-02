e=enumerate
def p(g):
 for i,v in e(g):
  for j,w in e(v):
   for I,V in e(g):
    for J,W in e(V):
     if i+1<I and j+1<J and v[j:J+1]==V[j:J+1]==[1]*(J+1-j) and all(u[j:J+1]==[1]+[0]*(J-1-j)+[1]for u in g[i+1:I]):
      v[j:J+1]=V[j:J+1]=[3]*(J+1-j)
      for u in g[i+1:I]:u[j:J+1]=[3]+[0]*(J-1-j)+[3]
 return g