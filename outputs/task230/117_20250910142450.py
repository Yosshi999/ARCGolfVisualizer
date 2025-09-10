def p(g):
 for c in b'':r=range(len(g));g=[[g[j][~i]+c*(g[j-2][1-i]>4<g[j-1][-i])for j in r]for i in r]
 return g