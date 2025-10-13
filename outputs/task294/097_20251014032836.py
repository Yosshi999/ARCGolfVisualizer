r=range(10)
p=lambda g:[g:=[[5*(v[~i]>v[-i]*i)or v[~i]>>(t<1)for v in g]for i in r]for t in r][7]