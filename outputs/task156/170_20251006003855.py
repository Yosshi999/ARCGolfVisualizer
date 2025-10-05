e=enumerate
p=lambda g:[[v[j]-sum(v[j-1:j+2]+w[i-1:i+2])//24*(3-(2*sum(sum(g[:(I:=g.index(min(g),1))],[]))<sum(sum(g,[])))^(i<I))for j,(*w,)in e(zip(*g))]for i,v in e(g)]