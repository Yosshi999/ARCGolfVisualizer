r=range(30)
def p(g):
 for _ in[s:=[]]*4:g[::-1]=zip(*g);s=[(s,29-r,29-l,u,d)for s,u,d,l,r in s]+[((b-a+5)*w,-1,w,a,b)for a in r for b in r if(f:=1)for w in r if(f:=f*~-any(g[w][a:b+1]))]
 _,u,d,l,R=max(s);g=[[3*(u<i<d)*(l<j<R)+g[i][j]for j in r]for i in r];return[g:=[*zip(*[([3]*(j:=bytes(v:=[*g[i]]).find(3))+v[j:],v)[any(sum(u[:j])for u in g[i-(i>0):i+2])]for i in r])][::-1]for _ in g][3]