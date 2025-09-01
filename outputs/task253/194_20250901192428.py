def p(g):
 m=[0,0,0,0]
 for k in range(144):
  i=k//12;j=k%12;v=g[i][j:j+2]+g[i+1][j:j+2]
  if v.count(0)<2:m[3-v.index(0)]=v
 for d in[0,2]:a=m[d][2:];m[d][2:]=m[d+1][:2];m[d+1][:2]=a
 return m