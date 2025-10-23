e=enumerate
def p(g):
 W=len(g[0]);C=sorted(G:=sum(g,[]),key=G.count)[:2];m=[]
 for y,v in e(g):
  for x,w in e(zip(*g)):
   if(c:=g[y][x])in C:
    if len(s:={*w})==2:u={max(s-{c}):c,c:c};t=sum(C)-c
    if len(s:={*v})==2:u={max(s-{c}):c,c:c};t=sum(C)-c
    m+=y+x,x-y-W
 return[[any({y+x,x-y-W}&{*m})*u.get(a,t)or a for x,a in e(v)]for y,v in e(g)]