r=range
def p(g):
 for u in r(196):
  if{*g[s:=u//14][(t:=u%14):t+7]+g[s+6][t:t+7]}=={5}:
   for k in r(256):
    if all(g[(i:=k//16)+(I:=K//5)][(j:=k%16)+(J:=K%5)]==(g[s+1+I][t+1+J]>0)for K in r(25)):
     for d in r(5):g[i+d][j:j+5]=g[s+1+d][t+1:t+6]
 return g