exec("""def p(g):
 for _ in[s:=[]]*4:g=[*zip(*g)][::-1];s=[(s,29-r,29-l,u,d)for s,u,d,l,r in s]+[((b-a+5)*w,-1,w,a,b)@@if(f:=1)@if(f:=f*~-any(g[w][a:b+1]))]
 _,u,d,l,R=max(s);g=[[3*(u<i<d)*(l<j<R)+g[i][j]@]@];return[g:=[*zip(*[([3]*(j:=bytes(v:=[*g[i]]).find(3))+v[j:],v)[any(sum(u[:j])for u in g[i-(i>0):i+2])]@])][::-1]for _ in g][3]""".replace("@","for %s in range(30)")%(*'abwjii',))