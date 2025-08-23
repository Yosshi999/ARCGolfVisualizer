def p(g):
 [B:=s.pop()for v in g if len(s:=set(v)-{0})&1]
 C=(set(sum(g,[]))-{B,0}).pop()
 for _ in"..":g=[map(({C:B+10,0:C}if 0<v.count(B)<4else{}).get,v,v)for v in zip(*g)]
 return[[a%10for a in v]for v in g]