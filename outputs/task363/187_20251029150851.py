r=range(121)
p=lambda g:[[(G:=sum([v+[5]for v in g],[5]*11))[z:=y*11+x]|2*any(G[z-Z]&2>((Z in[23,51,79])<=G[40])>any(G[a-Z]==2<=G[a]for a in r)for Z in r)for x in r[:10]]for y in r[1:11]]