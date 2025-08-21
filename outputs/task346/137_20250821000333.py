e=enumerate
p=lambda g:[[[g[i+1][j+1]]]for i,v in e(g[:-2])for j,w in e(v[:-2])if{*(v[j:j+3]+g[i+1][j:j+3:2]+g[i+2][j:j+3])}=={w}-{0}][0]