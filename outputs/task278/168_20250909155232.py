e=enumerate
p=lambda g,d=8:d and p([*zip(*[[(2,2)in[g[y-1][x-2+k:x+k]for k in[0,1,2,3]if y]+[g[y][x+1:x+3]]and 3 or c for x,c in e(v)] for y,v in e(g)])][::-1],d-1)or g