e=enumerate
def p(g):
 for i,v in e(g[:-2]):
  for j,w in e(v[:-2]):
   if w and v[j:j+3]==g[i+2][j:j+3]==[w,0,w]and g[i+1][j+1]==w:H=2*i+2;W=2*j+2
 for _ in'..':g=[[w or 0<=H-j<len(v)and v[H-j]for j,w in e(v)]for v in zip(*g)];H=W
 return g