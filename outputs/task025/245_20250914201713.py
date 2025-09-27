def p(g):
 if any(min(g)):return[*zip(*p([*zip(*g)]))]
 z=[min(g)]
 return [[u[0]*(u[0]in x[i:])for x in zip(*g)]if all(u)else v if all(v)else [w[0]*(w[0]in x[:i])for x in zip(*g)]if all(w)else z[0] for i,(u,v,w)in enumerate(zip(z+g,g,g[1:]+z))]