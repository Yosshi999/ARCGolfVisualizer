r=range(10)
def p(g):
 k=[i for i in r if g[9][i]][0]
 return[[(g[9][k],5*(i==(0,9)[(j-k&3)>>1]))[j-k&1]if j>=k else 0for j in r]for i in r]