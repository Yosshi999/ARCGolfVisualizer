def p(g):
 s=len(g)
 o=[[0]*s for _ in range(s)]
 r,c,dr,dc=0,0,0,1
 while True:
  if o[r][c]==3: break
  if r+dr>=0 and r+dr<s and c+dc>=0 and c+dc<s:
   if o[r+dr][c+dc]==3: break
  o[r][c]=3
  if dc==1 and c+1==s:
   dr,dc=1,0
  elif dc==1 and c+2<s and o[r][c+2]==3:
   dr,dc=1,0
  elif dr==1 and r+1==s:
   dr,dc=0,-1
  elif dr==1 and r+2<s and o[r+2][c]==3:
   dr,dc=0,-1
  elif dc==-1 and c==0:
   dr,dc=-1,0
  elif dc==-1 and c-2>=0 and o[r][c-2]==3:
   dr,dc=-1,0
  elif dr==-1 and o[r-2][c]==3:
   dr,dc=0,1
  c+=dc
  r+=dr
 return o