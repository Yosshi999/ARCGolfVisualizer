def p(g):
 cnt=[0]*10
 for v in g:
  for a in v:cnt[a]+=1
 res=[x for i in[10,8,6,4,2]for x in range(10) if cnt[x]==i]
 return[*map(list,zip(*[res]))]