R=range
def D(g,y,x):
 if 9>=y>0<=x<15>g[y][x]==5:g[y][x]=0;return[(y,x)]+sum((D(g,y+a%3-1,x+a//3-1)for a in R(9)),[])
 return[]
def F(A):(u,*_),(l,*_,r)=map(sorted,zip(*A));return(r-l+1,{(i-u,j-l)for(i,j)in A})
def G(g,l,A):
 for i,(w,a)in enumerate(A):
  for L in R(l,16-w):
   h=[*map(list,g)];m=max(sum(v[L+j]==2 for v in h)-min(i for i,J in a if j==J)for j in R(w))
   for y,x in a:h[y+m][L+x]=1
   if(r:=G(h,L+w,A[:i]+A[i+1:]))[0]:return r
 return(all(sum(g[:3],[])),g)
p=lambda g:G(g,0,[F(D(g,9,j))for j in R(15)if g[9][j]==5])[1]