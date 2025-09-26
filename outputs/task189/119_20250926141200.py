r=b''
p=lambda g:(0<g[0][0]!=3)*[[g[i>5][j>5]*g[i][j]/3for j in r]for i in r]or[*zip(*p([*zip(*g[::-1])]))][::-1]