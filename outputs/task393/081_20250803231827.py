def p(g):
 h=sum(g,[])
 return [[v]for v in sorted(set(h),key=h.count)][::-1][1:]