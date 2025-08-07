r=range(10)
f=lambda g,h:[[x or y*2for x,y in zip(*v)]for v in zip(g,h)]
s=lambda g:sum(sum(g,[]))
def p(g):
 A=[[g[-i][-j]for j in r]for i in r]
 B=[v[::-1]for v in g[::-1]]
 C=f(g,A)
 D=f(g,B)
 return(C,D)[s(C)>s(D)]