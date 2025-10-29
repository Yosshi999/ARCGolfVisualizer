e=enumerate
def p(g):
 C=sorted(G:=sum(g,m:=[]),key=G.count)[:2]
 for y,v in e(g+[*zip(*g)]):
  for x,c in e(v):
   if c in C:
    if len({*v})<3:u=v;t=sum(C)-c,c
    if v in g:m+=y+x,y-x-99
 return[[any({y+x,y-x-99}&{*m})*t[a in u]or a for x,a in e(v)]for y,v in e(g)]