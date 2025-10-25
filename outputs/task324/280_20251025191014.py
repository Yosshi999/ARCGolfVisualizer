e=enumerate
def p(g):
 C=sorted(G:=sum(g,m:=[]),key=G.count)[:2]
 for y,v in e(g):
  for x,w in e(zip(*g)):
   if(c:=v[x])in C:
    for z in v,w:
     if len({*z})==2:u=z;t=sum(C)-c,c
    m+=y+x,x-y-99
 return[[any({y+x,x-y-99}&{*m})*t[a in u]or a for x,a in e(v)]for y,v in e(g)]