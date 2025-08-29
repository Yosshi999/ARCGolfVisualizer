r=range
f=lambda G:3+sum([y*3for y in[-1,1]if G[y+1][1]-5])
def p(g):
 h=[[0]*9for _ in r(9)]
 for i in r(len(g)-2):
  for j in r(len(g[0])-2):
   if all(map(all,G:=[u[j:j+3]for u in g[i:i+3]])):
    for t in r(9):h[f(G)+u][f([*zip(*G)])+v]=G[u:=t//3][v:=t%3]
 return h