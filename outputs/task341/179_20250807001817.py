def f(g):
 x=[v for v in g if len({*v})>2]
 for v in x[1:-1]:
  j=0
  while v[j]<1:j+=1
  while v[j]:j+=1
  while v[j]<1:v[j]=8;j+=1
 return[*map(list,zip(*g))]
p=lambda g:f(f(g))