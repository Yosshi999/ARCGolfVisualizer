r=range(9)
p=lambda g:[[3*(i//4==j//4<2)for j in r][::1|1-g[1][2]]for i in r][::1|1-g[2][1]]