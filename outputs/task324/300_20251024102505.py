e=enumerate
def p(g):
 C=sorted(G:=sum(g,[]),key=G.count)[:2];m=[]
 for y,v in e(g+[*zip(*g)]):
  for x,c in e(v):
   if c in C:
    if len({*v})==2:u={max({*v}-{t:=c}):c,c:c}
    if y<len(g):m+=y+x,y-x-len(g)
 return[[any({y+x,y-x-len(g)}&{*m})*u.get(a,sum(C)-t)or a for x,a in e(v)]for y,v in e(g)]