def p(g):
 A=[0];B=[0]
 for u in g[0]:
  if u!=A[-1]:A+=[u]
 for v in [*zip(*g)][0]:
  if v!=B[-1]:B+=[v]
 return [A[1:]]if len(A)>len(B)else [[v]for v in B[1:]]