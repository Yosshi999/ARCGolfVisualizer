r=range
I=lambda v,a:(v+[a]).index(a)
H=lambda g:sum([[I(v,8),I(v[::-1],8)] for v in g],[])+[min(I(v,0) for v in g)]
def p(g):
 h,m,q,D=0,[],set(),0
 for d in r(1,9):
  for y in r(len(g)-d):
   if all(map(any,(b:=g[y:y+d]))):
    h=max(h,d)
    if not(any(g[y-1])):q|={y}
    if any([any(v[-2:])for v in b]): m=[v[-2:]for v in b];o=[v[0]for v in b];O=H(b)
 for y in q:
  if [v[0] for v in g[y:y+h]]!=o: y-=1
  D=any(map(lambda x,y:abs(x-y)==1,O,H(g[y:y+h])))
  for x in r(len(g[0]))[::-1]:
   if any(g[y+t][x] for t in r(h)): break
   for d in r(h): g[y+d][x]=m[d][(x+D)%2]//8
 return g