def p(g):
 h,w=len(g),len(g[0])
 o=[r[:] for r in g]
 
 # Find horizontal pairs (same row)
 for r in range(h):
  cols_with_colors={}
  for c in range(w):
   if g[r][c]!=0:
    color=g[r][c]
    if color not in cols_with_colors:
     cols_with_colors[color]=[]
    cols_with_colors[color].append(c)
  
  # Draw lines between pairs of same color
  for color,cols in cols_with_colors.items():
   if len(cols)==2:
    c1,c2=min(cols),max(cols)
    for c in range(c1,c2+1):
     o[r][c]=color
 
 # Find vertical pairs (same column)
 for c in range(w):
  rows_with_colors={}
  for r in range(h):
   if g[r][c]!=0:
    color=g[r][c]
    if color not in rows_with_colors:
     rows_with_colors[color]=[]
    rows_with_colors[color].append(r)
  
  # Draw lines between pairs of same color
  for color,rows in rows_with_colors.items():
   if len(rows)==2:
    r1,r2=min(rows),max(rows)
    for r in range(r1,r2+1):
     o[r][c]=color
 
 return o