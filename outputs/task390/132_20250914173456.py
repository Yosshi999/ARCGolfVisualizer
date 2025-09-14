t=lambda v:v[:(k:=v.index(2)-3)+6:-1]+v[k:k+7]+v[:k][::-1]if{5,2}<{*v}else v
f=lambda g:[t(t(v))for v in zip(*g)]
p=lambda x:f(f(x))