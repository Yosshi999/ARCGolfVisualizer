def p(g,d=4):
 if{0,2}==set(v:=max(g[::-1],key=any)):g=[[c or 3for c in g[min(i,g.index(v)*2-i-1)]]for i in range(10)]
 return d and p([*zip(*g)][::-1],d-1)or g