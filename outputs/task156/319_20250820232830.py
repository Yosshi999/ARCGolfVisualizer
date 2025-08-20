e=enumerate
def p(g):
 a,*_,b=((i,j)for i,v in e(g)for j,x in e(v)if x);u,l=d,r=a;U,L=D,R=b
 while d<9and g[d+1][r]:d+=1
 while r<9and g[d][r+1]:r+=1
 while g[U-1][L]:U-=1
 while g[U][L-1]:L-=1
 return[[(x,1,2)[(u<i<d)*(l<j<r)*(1+(d+r-u-l>D+R-U-L))+(U<i<D)*(L<j<R)*(1+(d+r-u-l<D+R-U-L))]for j,x in e(v)]for i,v in e(g)]