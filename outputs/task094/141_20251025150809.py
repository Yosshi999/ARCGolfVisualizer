e=enumerate
p=lambda g:[g:=[[x-x//8*2*([1,1]==w[i-2:i+3:4]==v[j-2:j+3:4]or 6in v+w)for j,(*w,x)in e(zip(*g,v))]for i,v in e(g)]for _ in g][1]