e=enumerate
p=lambda g:[[v[j]or(0,2,0,4,6,3,0,1,0)[sum(v[:j])//8+sum(w[:i])//8*3]for j,w in e(zip(*g))]for i,v in e(g)]