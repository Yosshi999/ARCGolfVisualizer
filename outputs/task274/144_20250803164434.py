def p(g):
    c=0
    for v in g:
        c+=''.join(map(str,v)).count('050')
    c//=2
    return [[(c>0)*8,(c>1)*8,c//3*8],[0,0,c//4*8],[0]*3]