r=range(10)
p=lambda g:[g:=[[g[i][j]|max(g[I:=i-k][J:=j-k]*(I>0<J*g[I+1][J]*g[I][J+1])for k in r[2:])for i in r]for j in r][::-1]for _ in g][3]