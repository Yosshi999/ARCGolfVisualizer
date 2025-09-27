e=enumerate
p=lambda g:eval('[[v[~j]|v[j-2*(i+2<j<16-i)]for j,w in e(v)]for i,v in e(zip(*'*13+'g'+'[::-1]))]'*13)