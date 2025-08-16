e=enumerate
def p(g):
 for i,v in e(g):
  for j,w in e(v[:-2]):
   if(w>0)*len(set(v[j:j+3]+g[i+1][j:j+3:2]+g[i+2][j:j+3]))==1:return[[g[i+1][j+1]]]