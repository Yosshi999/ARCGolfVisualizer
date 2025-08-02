def p(g):
 c=len(g[0])
 return [[8]*c]+[[8]+[0]*(c-2)+[8]]*(len(g)-2)+[[8]*c]