def p(g):
 f=g.index;B=f(min(g),A:=f(max(g,key=any)));h=B-A;*G,=map(list,zip(*g))
 for i in range(15):
  if any(g[i])>any(g[i-1]):
   i-=G[0][i:i+h]!=G[0][A:B];D=max(x for x in range(-2,2)if~-any(any(w:=G[X][i:i+h])>(w==G[(X+x)%10][A:B])<X+x for X in range(10)))%2;q=1
   for w in G[::-1]:w[i:i+h*q]=map(bool,G[8+(D:=1-D)][A:B*(q:=q>any(w[i:i+h]))])
 return[*zip(*G)]