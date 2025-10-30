e=enumerate
p=lambda g:[[(a,8)[sum(v[j-1:j+2]+w[i-1:i+2])>5*a>0]for j,(*w,a)in e(zip(*g,v))]for i,v in e(g)]