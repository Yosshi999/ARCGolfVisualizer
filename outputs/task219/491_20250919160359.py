I=lambda v,a:(v+[a]).index(a)
H=lambda g:sum([[I(v,8),I(v[::-1],8)] for v in g],[])+[min(I(v,0) for v in g)]
def p(g):
 fr=g.index(max(g,key=any))
 to=g.index(min(g),fr)
 h=to-fr
 gt=[*map(list,zip(*g))]
 q=[i for i,v in enumerate(g)if any(v)>any(g[i-1])]
 for i in q:
  i-=gt[0][i:i+h]!=gt[0][fr:to]
  D=any(map(lambda x,y:abs(x-y)==1,H(g[fr:to]),H(g[i:i+h])))
  for j in range(len(gt))[::-1]:
   if any(gt[j][i:i+h]): break
   gt[j][i:i+h]=map(bool,gt[8+(j+D)%2][fr:to])
 return[*zip(*gt)]