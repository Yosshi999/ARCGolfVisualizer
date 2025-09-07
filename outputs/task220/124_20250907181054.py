e=enumerate
p=lambda g:[[w or((m:=max(max(v[j-(j>0):j+2])for v in g[i-(i>0):i+2]))/2,6)[m%2]for j,w in e(v)]for i,v in e(g)]