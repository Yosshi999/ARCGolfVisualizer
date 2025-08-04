def p(g):
 h,w=len(g),len(g[0])
 v=[[False]*w for _ in range(h)]
 def ff(sr,sc,tv):
  if sr<0 or sr>=h or sc<0 or sc>=w or v[sr][sc] or g[sr][sc]!=tv:return []
  v[sr][sc]=True
  co=[(sr,sc)]
  for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
   co.extend(ff(sr+dr,sc+dc,tv))
  return co
 b=[]
 for r in range(h):
  for c in range(w):
   if g[r][c]==2 and not v[r][c]:
    b.append(ff(r,c,2))
 if len(b)<2:return [[0]]
 v2=[[False]*w for _ in range(h)]
 def bfs(st,tg):
  q=st[:]
  for r,c in st:v2[r][c]=True
  while q:
   r,c=q.pop(0)
   for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
    nr,nc=r+dr,c+dc
    if nr<0 or nr>=h or nc<0 or nc>=w or v2[nr][nc] or g[nr][nc]==0:continue
    if (nr,nc) in tg:return True
    v2[nr][nc]=True
    q.append((nr,nc))
  return False
 cv=0
 for r in range(h):
  for c in range(w):
   if g[r][c]!=0 and g[r][c]!=2:cv=g[r][c];break
 return [[cv if bfs(b[0],b[1]) else 0]]