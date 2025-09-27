e=enumerate
p=lambda g:[g:=[[w[~i]+c*(g[j-2][1-i]>4<g[j-1][-i])for j,w in e(g)]for i,v in e(g)]for c in b''][3]