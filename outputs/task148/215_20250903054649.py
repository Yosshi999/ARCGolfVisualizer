def f(g):
 W=len(g[0])-1;Y=[]
 return[(([2]+[8]*((c:=v.index(8))-1)+[4]+[0]*(W-c)if v.count(8)==1else v,Y:=Y+[8 in v])[0]if v[0]else([8]*W+[2])if v[-1]==2and Y and Y.pop(0)else v)[::-1]for v in g]
p=lambda g:f(f(g))