e=enumerate
p=lambda g:[g:=[t*[w or(g[j-1][i-1]%8*i*j>0)*8for j,w in e(v)]for i,v in e(zip(*g))][::-1]for t in[2,2]+[1]*6][7]