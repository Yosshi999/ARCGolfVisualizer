r=range(10)
f=lambda g,h:[[x or y*2for x,y in zip(*v)]for v in zip(g,h)]
s=lambda g:sum(sum(g,[]))
def p(g):
 return(C:=f(g,[[g[-i][-j]for j in r]for i in r]),D:=f(g,[v[::-1]for v in g[::-1]]))[s(C)>s(D)]