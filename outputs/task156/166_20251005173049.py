e=enumerate;s=sum
p=lambda g:[[v[j]-s(v[j-1:j+2]+w[i-1:i+2])//24*((i<(I:=g.index(min(g),1)))^3-(s(G:=s(g,[]))>2*s(G[:10*I])))for j,(*w,)in e(zip(*g))]for i,v in e(g)]