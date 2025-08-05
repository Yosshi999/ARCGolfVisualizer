def p(g):
 s=[[0]*3for j in[0]*3];h=0
 for _ in[0]*(sum(sum(g,[]))//8):s[h//3][h%3]=1;h+=2
 return s