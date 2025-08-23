e=enumerate
p=lambda g:[[max(v[j],(i in[3,4])*min(w[i-3::6]),(j in[3,4])*min(v[j-3::6]))for j,w in e(zip(*g))]for i,v in e(g)]