t=lambda v:v[(k:=v.index(2)-3)+7:][::-1]+v[k:k+7]+v[:k][::-1]if{5,2}<={*v}else v
f=lambda g:[*map(list,zip(*[t(t(v))for v in g]))]
p=lambda x:f(f(x))