def p(g):
 fr=g.index(max(g,key=any))
 to=g.index(min(g),fr)
 h=to-fr
 gt=[*map(list,zip(*g))]
 q=[i for i,v in enumerate(g)if any(v)>any(g[i-1])]
 for i in q:
  i-=gt[0][i:i+h]!=gt[0][fr:to]
  D=max(x for x in range(-3,9)if all(any(v:=gt[X][i:i+h])<1 or X+x<0 or v==gt[(X+x)%10][fr:to]for X in range(10)))
  for j in range(len(gt))[::-1]:
   if any(gt[j][i:i+h]): break
   gt[j][i:i+h]=map(bool,gt[8+(j+D)%2][fr:to])
 return[*zip(*gt)]