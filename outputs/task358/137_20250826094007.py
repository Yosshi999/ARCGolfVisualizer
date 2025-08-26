f=lambda g:[*zip(*[[max(v[j%(d:=len(v)-v.count(0))::d])for j in range(len(v))]if v==max(g,key=sum)else v for v in g])]
p=lambda g:f(f(g))