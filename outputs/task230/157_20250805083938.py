def f(g,c):r=range(len(g));return[*map(list,zip(*[[(g[i][j],c)[g[i-2][j-2]*(g[i-1][j-1]>4)>4]for j in r]for i in r][::-1]))]
p=lambda g:f(f(f(f(g,4),2),1),3)