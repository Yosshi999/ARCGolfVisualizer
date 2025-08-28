def p(g):
 g=eval(str([*zip(*g)]).replace('0, 5, 0','1,2,1'))
 g=eval(str([*zip(*g)]).replace('0, 1, 0','5,1,5').replace('0, 2, 0','1,0,1'))
 return g