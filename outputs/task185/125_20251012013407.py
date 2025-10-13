f=lambda h,g:[(y:=0)or[x*(y==(y:=x)!=max(h[0]))for w,x in zip(g,v)if{*w}-{*h[0]}][1:]for v in zip(*g)]
p=lambda g:f(g,f(g,g))