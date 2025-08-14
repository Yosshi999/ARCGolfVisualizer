def p(g):
 for i in range(9):
  for j in range(9):
   if g[i][j]==2:
    for k in range(9):
     if i-k>=0and j-k>=0and g[i-k][j-k]==5:
      g[i-1][j-1]=5;g[i-k][j-k]=0
     if j-k>=0:
      if g[i][j-k]==5:
       g[i][j-1]=5;g[i][j-k]=0
      if g[i+1][j-k]==5:
       g[i+1][j-1]=5;g[i+1][j-k]=0
     if i+1+k<10and j-k>=0and g[i+1+k][j-k]==5:
      g[i+2][j-1]=5;g[i+1+k][j-k]=0
     if i+1+k<10:
      if g[i+1+k][j]==5:
       g[i+2][j]=5;g[i+1+k][j]=0
      if g[i+1+k][j+1]==5:
       g[i+2][j+1]=5;g[i+1+k][j+1]=0
     if i+1+k<10and j+1+k<10and g[i+1+k][j+1+k]==5:
       g[i+2][j+2]=5;g[i+1+k][j+1+k]=0
     if j+1+k<10:
      if g[i][j+1+k]==5:
       g[i][j+2]=5;g[i][j+1+k]=0
      if g[i+1][j+1+k]==5:
       g[i+1][j+2]=5;g[i+1][j+1+k]=0
     if i-k>=0and j+1+k<10and g[i-k][j+1+k]==5:
      g[i-1][j+2]=5;g[i-k][j+1+k]=0
     if i-k>=0:
      if g[i-k][j]==5:
       g[i-1][j]=5;g[i-k][j]=0
      if g[i-k][j+1]==5:
       g[i-1][j+1]=5;g[i-k][j+1]=0
    return g