r=range(10)
p=lambda g:[[g[i][j]or(2in{*g[i][:j]}&{*g[i][j:]})*(0!=i!=9)*9for j in r]for i in r]