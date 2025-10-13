t=lambda v:v[:(k:=v.index(2)-3)+6:-1]+v[k:k+7]+v[:k][::-1]if{5,2}<{*v}else v
p=lambda g:eval('[t(t(v))for v in zip(*'*2+'g)])]')