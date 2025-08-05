def p(g):
 for c in[4,2,1,3]:r=range(len(g));g=[*map(list,zip(*[[(g[i][j],c)[g[i-2][j-2]*(g[i-1][j-1]>4)>4]for j in r]for i in r][::-1]))]
 return g