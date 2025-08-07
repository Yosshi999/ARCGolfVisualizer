e=enumerate
def p(g):
 z=[[0]*(len(g[0])+2)]
 g=z+[[0]+v+[0]for v in g]+z
 for _ in[0,0]:
  for i,v in e(g):
   for j,w in e(v):
    if v[j:j+2]==[2,2]:
     for k in[-1,0,1]:g[i+k][j-1:j+3]=[3]*4
     v[j:j+2]=[2,2]
  g=[*map(list,zip(*g))]
 return[v[1:-1]for v in g[1:-1]]