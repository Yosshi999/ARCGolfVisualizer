f=lambda g:[[max(w[i%10::10])for i in range(len(w))]for w in zip(*g)]
p=lambda g:f(f(g))