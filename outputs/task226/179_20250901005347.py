e=enumerate
f=lambda x:x.count(5)
p=lambda g:[[v[j]or(a:=f(v[:j]),b:=f(v[j:]),c:=f(w[:i]),d:=f(w[i:]),(a==c<1)+(b==d<1)*3+(a==b)*(c==d)*2)[4]for j,w in e(zip(*g))]for i,v in e(g)]