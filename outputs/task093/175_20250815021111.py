q=lambda g:[[*v]if len({*v})<3 else(l:=min(i for i in range(14)if v[i]==5),a:=v[:l].count(0),b:=v[l:].count(0),[0]*a+[5]*(14-a-b)+[0]*b)[3]for v in zip(*g)]
p=lambda g:q(q(g))