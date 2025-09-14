def p(g):
 g=[[0,*v,0]for v in g*2]
 g[i:=g.index(v:=max(g))][j:=v.index(2)]=0
 g[i-1][j-1:j+2]=[3,0,6]
 g[i+1][j-1:j+2]=[8,0,7]
 return[v[1:6]for v in g[:3]]