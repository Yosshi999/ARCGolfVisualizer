q=lambda G:[v for v in zip(*G)if{*v}-{0,2}]
p=lambda g:(r:=lambda G:[[2]+sum([sum(g,[]).count(2)//12*[w]for w in v],[])+[2]for v in zip(*G)])(r(q(q(g))))