e=enumerate
p=lambda g:[[v[j]or(a:=v[:j].count(5),b:=v[j:].count(5),c:=w[:i].count(5),d:=w[i:].count(5),(a==c<1)+(b==d<1)*3+(a==b)*(c==d)*2)[4]for j,w in e(zip(*g))]for i,v in e(g)]