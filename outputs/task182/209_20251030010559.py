r=range
def p(g):
 u=str(g).rfind('5');s=u//62;t=u%62//3
 for k in r(256):
  for d in r(5*all(g[(i:=k//16)+K][(j:=k%16):j+5]==[*map(bool,g[s-5+K][t-5:t])]for K in r(5))):g[i+d][j:j+5]=g[s-5+d][t-5:t]
 return g