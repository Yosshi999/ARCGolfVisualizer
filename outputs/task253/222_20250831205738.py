t=lambda g:[*map(list,zip(*g[::-1]))]
def p(g):
 z=[0]*4;h=[[*z]for _ in z]
 for _ in z:
  for k in range(144):
   i=k//12;j=k%12;c=g[i+1][j]
   if g[i][j:j+2]==[c,c]and c:h[0][:2]=[c,c];h[1][0]=c
  g=t(g);h=t(h)
 return h