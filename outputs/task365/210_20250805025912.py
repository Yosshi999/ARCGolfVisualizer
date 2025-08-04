r=range(11)
def p(g):
 h=[]
 for i in r:
  for j in r:
   for k in r:
    for l in r:
     if min((Q:=sum(q:=[v[j:l]for v in g[i:k]],[]))+[1]):h+=[(q,Q)]
 return max(h,key=lambda x:(x[1].count(2),len(x[1])))[0]