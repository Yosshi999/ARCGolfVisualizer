def p(g):
 h=[[a for*w,a in zip(*g,v)if 8in w]for v in g if 8in v];g=[[a for*w,a in zip(*g,v)if{*w}-{0,8}]for v in g if{*v}-{0,8}];n=len(h)
 for i in range(n):
  for j in range(n):f=(j-i)*(n-1-i-j);g[i+1][j+1]=(g[1][0-2*j//n],8,g[0-2*i//n][1])[(f>0)+(f>=0)]*(h[i][j]>0)
 return g