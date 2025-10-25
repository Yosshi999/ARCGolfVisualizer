e=enumerate
def p(g):
 C=sorted(G:=sum(g,[]),key=G.count)[:2];m=[]
 for y,v in e(g):
  for x,w in e(zip(*g)):
   if(c:=g[y][x])in C:
    for z in v,w:
     if len(s:={*z})==2:u=s;t=sum(C)-c,c
    m+=y+x,x-y-99
 return[[any({y+x,x-y-99}&{*m})*t[a in u]or a for x,a in e(v)]for y,v in e(g)]