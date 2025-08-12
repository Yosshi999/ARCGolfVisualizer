t=lambda g:[*zip(*g)]
e=enumerate
r=range
p=lambda g:(g:=t([[a|1if 9in v[:x]else a for x,a in enumerate(v)]for v in t(g)]),s:={0},[[(w:=0,[w:=d//2 for d in r(50)if d*(9,)in[v[x:x+d],v[x-d+1:x+1]]],[s:=s|{(q,p)}for p in r(x-w,x+w+1) for q in r(y-w,y+w+1)if w])for x,a in e(v)]for y,v in e(g)],[[3 if(y,x)in s and a<9else a for x,a in e(v)]for y,v in e(g)])[3]