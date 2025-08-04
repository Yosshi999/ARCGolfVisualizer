def p(g):
    c=0
    l=[0]*9
    for j in range(10):
        for v in g:
            if v[j]:
                l[c]=v[j]
                c+=1
    return [l[:3],l[3:6][::-1],l[6:]]