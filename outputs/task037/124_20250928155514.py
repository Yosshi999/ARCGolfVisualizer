r=range(10)
p=lambda g:[[max(e for d in[9,11]for e in{*sum(g,[])[10*i+j::d]}&{*sum(g,[])[10*i+j::-d]})for j in r]for i in r]