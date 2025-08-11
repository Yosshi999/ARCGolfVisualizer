e=enumerate
f=lambda g:[*map(list,zip(*[(t:=0,[(t*2|c,t:=(c==2 and 8 in v[x:])or(t and c!=8))[0]for x,c in e(v)])[1]for v in g]))][::-1]
p=lambda g:(t:=f(f(f(f(g)))),[[(2 if c>9 else 8 if 10 in sum([w[max(0,x-1):x+2]for w in t[max(0,y-1):y+2]],[])else c) for x,c in e(v)]for y,v in e(t)])[1]