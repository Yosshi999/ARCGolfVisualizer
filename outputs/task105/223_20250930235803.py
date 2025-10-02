e=enumerate
def p(g,d=3):
 l,*_,r=sorted(i for i,v in e(g)if any(v));m=0;g=[*map(list,zip(*g))][::-1]
 for i,v in e(g):
  if len([*filter(int,v)])>m:
   m=3
   for j,w in e(v[l:r+1]):v[j+l]=w or 2
 return d and p(g,d-1)or g