e=enumerate
p=lambda g:[[max(g[I+1][J+~((d:=(V[J+3]>0)+2)>i-I>0<j-J<d)+(0<=i-I<=d>J-j>-2*d)+(0<=j-J<=d>I-i>-2*d)]for I,V in e(g)for J,W in e(V)if W>0>=V[J-1]+g[I-1][J])for j,w in e(v)]for i,v in e(g)]