f=lambda g:[*map(list,zip(*g[::-1]))]
def p(g):h=[v[:3]for v in g[:3]];return[a+[5]+b+[5]+c for a,b,c in zip(h,f(h),f(f(h)))]