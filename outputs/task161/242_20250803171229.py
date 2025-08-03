def p(g):
    for i in range(10):
        if sum(g,[]).count(i)==4 and sum([v[1:-1]for v in g[1:-1]],[]).count(i)==0:
            c=i
    return [[c if v[0]==c or v[-1]==c or g[0][j]==c or g[-1][j]==c else 0 for j in range(len(v))]for v in g]