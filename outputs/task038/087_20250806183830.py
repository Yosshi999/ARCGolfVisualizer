def p(g):
 s=sum(''.join(map(str,v)).count('11')for v in g)//2
 return[[1]*s+[0]*(5-s)]