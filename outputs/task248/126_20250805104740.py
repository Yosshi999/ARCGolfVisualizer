def p(g):
 h=len(g);w=len(g[0])
 return[[((h-i-1-j)%(2*(w-1))==0)|((h-1-i+j)%(2*(w-1))==0)for j in range(w)]for i in range(h)]