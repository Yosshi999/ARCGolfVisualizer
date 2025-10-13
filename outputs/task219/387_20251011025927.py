def p(g):
 f=g.index
 A=f(max(g,key=any))
 B=f(min(g),A)
 h=B-A
 G=[*map(list,zip(*g))]
 for i in range(15):
  if any(g[i])>any(g[i-1]):
   i-=G[0][i:i+h]!=G[0][A:B]
   D=max(x for x in range(-2,2)if all(any(w:=G[X][i:i+h])<1 or X+x<0 or w==G[(X+x)%10][A:B]for X in range(10)))%2
   for w in G[::-1]:
    if any(w[i:i+h]):break
    w[i:i+h]=map(bool,G[8+(D:=1-D)][A:B])
 return[*zip(*G)]