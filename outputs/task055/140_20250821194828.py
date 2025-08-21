e=enumerate
p=lambda g:[[(0,2,0,4,6,3,0,1,0)[v[:j].count(8)+w[:i].count(8)*3]if 0in v and 0in w else 8for j,w in e(zip(*g))]for i,v in e(g)]