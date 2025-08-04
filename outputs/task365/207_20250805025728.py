r=range(11)
def p(g):
 h=[]
 for i in r:
  for j in r:
   for k in r:
    for l in r:
     if min(sum(q:=[v[j:l]for v in g[i:k]],[])+[1]):h+=q,
 return max(h,key=lambda x:(sum(x,[]).count(2),len(sum(x,[]))))