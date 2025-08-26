e=enumerate
p=lambda g:[[w<any(2in v[j-(j>0):j+2]for v in g[i-(i>0):i+2])or w for j,w in e(v)]for i,v in e(g)]