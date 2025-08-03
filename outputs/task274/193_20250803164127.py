def p(g):
    c=0
    for v in g:
        for j in range(len(v)):
            if v[j]and v[j-1]+v[j+1]<1:
                c+=1
    c//=2
    return [[(c>0)*8,(c>1)*8,c//3*8],[0,0,c//4*8],[0]*3]