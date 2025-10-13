q=lambda G,c:[sum([c*[w]for w in v],[2])+[2]for v in zip(*G)if{*v}-{0,2}or{*v}=={2}]
p=lambda g:q(q(g,c:=sum(g,[]).count(2)//12),c)