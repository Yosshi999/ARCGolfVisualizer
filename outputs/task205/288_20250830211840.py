def p(g):
 h=max((len(H),h)for i in range(len(g))for j in range(len(g[0]))for k in range(len(g))for l in range(len(g[0]))if len(set(H:=sum(h:=[v[j:l]for v in g[i:k]],[])))<3)[1]
 c,d=sorted({*sum(h,[])},key=sum(h,[]).count)
 print(c,d)
 return[[(d,c)[c in v+w]for*w,in zip(*h)]for v in h]