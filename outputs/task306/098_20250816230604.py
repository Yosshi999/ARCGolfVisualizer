e=enumerate
p=lambda g:[[max(max(x[j%10::10])for x in g[i%10::10])for j,w in e(v)]for i,v in e(g)]