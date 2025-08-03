def p(g):
    return(h:=[v+w for v,w in zip(g,map(list,zip(*g[::-1])))])+[v[::-1]for v in h[::-1]]