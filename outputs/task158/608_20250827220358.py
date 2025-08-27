def p(g):
 for s in range(len(g)-2):
  for t in range(len(g[0])-2):
   h=[v[t:t+3]for v in g[s:s+3]]
   if len({*sum(h,[])})<4:continue
   print(h)
   if h[0][0]==h[2][2]:h=h[::-1]
   for _ in'....':
    for k in 3,2,1:
     for i in range(len(g)-3*k+1):
      for j in range(len(g[0])-3*k+1):
       if all({*v[j:j+k]}=={h[0][0]}for v in g[i:i+k]) and all({*v[j+2*k:j+3*k]}=={h[2][2]}for v in g[i+2*k:i+3*k]) and g[i-1][j-1]==max(sum(g,[]),key=sum(g,[]).count):
        print(i,j)
        for x in range(3*k):
         for y in range(3*k):g[i+x][j+y]=h[x//k][y//k]
    g=[*map(list,zip(*g[::-1]))]
 return g