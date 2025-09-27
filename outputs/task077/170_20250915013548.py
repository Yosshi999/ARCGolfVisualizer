e=enumerate
def p(g):
 for _ in[0]*6:g=[[2*(v[j]==2)or(sum(e in[2,4]for e in v[j-(j>0):j+2]+w[i-(i>0):i+2])>1)*4or v[j]for j,(*w,)in e(zip(*g))]for i,v in e(g)]
 return g