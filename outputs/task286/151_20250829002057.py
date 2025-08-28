def p(g):
 b,c={*sum(g,[])}-{0,8}
 for _ in[0]*200:
  for _ in'..':g=eval(str(g).replace(f'{b}, 0',f'{b}, {c}'));b,c=c,b
  g=[*zip(*g[::-1])]
 return g