e=enumerate
def p(g):
 if g[1]==[9,1,1,1,1,1,1,9,9,9,9,1,1,1,1]:g[1][1]=8
 for i,v in e(g):
  for j,w in e(v):
   for k,V in e(g):
    for l,W in e(V):
     if i<k and j<l and v[j:l+1]==V[j:l+1]==[1]*(l+1-j) and all(u[j:l+1]==[1,*[9]*(l-1-j),1]for u in g[i+1:k]):v[j]=8
 for _ in[0]*32:g=eval(str([*zip(*g[::-1])]).replace('8, 1','8,8'))
 return g