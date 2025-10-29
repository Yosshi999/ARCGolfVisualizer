r=range
def p(g):
 for u in r(196):
  for k in r(256*all(g[s:=u//14][(t:=u%14):t+7]+[g[s+1][t]])):
   for d in r(5*all(g[(i:=k//16)+K][(j:=k%16):j+5]==[*map(bool,g[s+1+K][t+1:t+6])]for K in r(5))):g[i+d][j:j+5]=g[s+1+d][t+1:t+6]
 return g