def p(g):
 for c in[4,3,1,2]:r=range(len(g));g=[[(g[j][i],c)[g[j-2][i-2]*(g[j-1][i-1]>4)>4]for j in r]for i in r][::-1]
 return g