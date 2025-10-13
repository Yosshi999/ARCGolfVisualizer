r=range(12)
p=lambda g:[[sum(u[i%2*2+j%2]for x in r for y in r if(u:=g[x][y:y+2]+g[x+1][y:y+2]).count(0)==1>u[3-i//2*2-j//2])for j in r[:4]]for i in r[:4]]