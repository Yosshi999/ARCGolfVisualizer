r=range(12)
p=lambda g:[[sum(u[x==y]for I in r for J in r if max(x:=abs(I-i),y:=abs(J+1-j))<=2*all(u:=g[I][J:J+3])!=x*y)for j in r]for i in r]