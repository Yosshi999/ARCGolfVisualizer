e=enumerate
p=lambda g:[[(a,8)[sum(v[j-(j>0):j+2]+w[i-(i>0):i+2])==6*a>0]for j,(*w,a)in e(zip(*g,v))]for i,v in e(g)]