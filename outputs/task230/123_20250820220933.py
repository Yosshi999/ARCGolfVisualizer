def p(g):
 for c in[3,1,2,4]:r=range(len(g));g=[[(g[j][~i],c)[g[j-2][1-i]*(g[j-1][-i]>4)>4]for j in r]for i in r]
 return g