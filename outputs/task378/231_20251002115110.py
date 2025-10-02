def f(g):
 r=range(len(g))
 for i in r:
  for j in r:
   d=sum([w[j:j+3:2]for w in g[i:i+3:2]],[]);I=i
   while j>0<I>0<all(d)<len(d)>2>d.count(d[3]):j-=1;I-=1;g[I][j]=d[3]
 return[*map(list,zip(*g))][::-1]
p=lambda g:f(f(f(f(g))))