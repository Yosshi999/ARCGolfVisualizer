f=lambda g,s,t:eval(str([*zip(*g)]).replace(s,t))
p=lambda g:f(f(f(f(g,'0, 5, 0','1,2,1'),'0, 1, 0','5,1,5'),'',''),'0, 2, 0','1,0,1')