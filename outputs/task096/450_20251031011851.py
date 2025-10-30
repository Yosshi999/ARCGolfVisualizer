def p(i):
 d=sum(i,[]);o=max(d,key=d.count);e={}
 for j in range(6):
  for m in{*d}:
   for n in range(20):
    for p in range(20):
     a={(abs(d-n),abs(r-p+1)):m for d,o in enumerate(i)for r,e in enumerate(o)if e==m}
     if m not in e.values()and{*map(max,a)}=={j}and all((abs(d-n),abs(r-p+1))not in a for d,o in enumerate(i)for r,e in enumerate(o)if e!=m):e|=a
 a=max(max(e));r=range(-a,a+1);return[[e.get((abs(d),abs(r)),o)for r in r]for d in r]