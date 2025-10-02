def f(g):r=range(len(g));return[[g[i][j]|max(i>=k+3<=j>0<all(d:=g[i-k-3][j-k-3:j-k:2]+g[i-k-1][j-k-3:j-k:2])==d.count(d[0])and d[0]for k in r)for i in r]for j in r][::-1]
p=lambda g:f(f(f(f(g))))