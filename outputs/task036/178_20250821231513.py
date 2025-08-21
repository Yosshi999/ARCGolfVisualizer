e=enumerate
def p(g):
 x=[]
 for c in{*sum(g,[])}:
  x+=[[a for*w,a in zip(*g,v)if c in w]for v in g if c in v],
 return min(x,key=lambda x:(sum(e>0for e in sum(x,[]))<5,len(x)))