r=range(9)
p=lambda g:[[min((I:=abs(i-x),J:=abs(j-y),-~-(d!=2!=(c:=d)>0<I+J)*(2>I-J>-2))for x in r for y in r if(d:=g[x][y]))[2]*c for j in r]for i in r]