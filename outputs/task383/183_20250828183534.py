def p(g):
 [B:=s.pop()for v in g if len(s:=set(v)-{0})&1]
 C=(set(sum(g,[]))-{B,0}).pop()
 return[[(B,C)[a<1]if 0<v.count(B)<4 or 0<w.count(B)<4else a for*w,a in zip(*g,v)]for v in g]