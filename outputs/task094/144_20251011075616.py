e=enumerate
p=lambda g:[g:=[[x-2*([1,8,8,8,1]==w[i-2:i+3]==v[j-2:j+3]or 6in v+w)*(x>7)for j,(*w,x)in e(zip(*g,v))]for i,v in e(g)]for _ in g][1]