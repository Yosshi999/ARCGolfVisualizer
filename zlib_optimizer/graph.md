```python

def p(g):
 i=0
 h=[v==i for u in g for v in u]
 c=sum(h)
 g=[[v * c + i for v in u] for u in g]
 return g

```
__main__
```mermaid
graph TB
  N2789306630928["ld() st() LO() ENV()"]
  N2789306630928 --> N2789306632400
  N2789306632400["ld() st(p) LO() ENV()"]
```
anon-0
```mermaid
graph TB
  N2789306632208["ld(g,i) st() LO(g,i) ENV()"]
  N2789306632208 --> N2789306632528
  N2789306632528["ld(g) st() LO(i) ENV()"]
  N2789306632528 --> N2789306635088
  N2789306635088["ld() st(u) LO(i,u) ENV(u)"]
  N2789306635088 --> N2789306634960
  N2789306634960["ld(u) st() LO(i) ENV(u)"]
  N2789306634960 --> N2789306636880
  N2789306636880["ld() st(v) LO(i,v) ENV(u,v)"]
  N2789306636880 --> N2789306637008
  N2789306637008["ld(v) st() LO(i) ENV(u,v)"]
  N2789306637008 --> N2789306632720
  N2789306632720["ld(i) st() LO() ENV(u,v)"]
```
anon-2
```mermaid
graph TB
  N2789306708368["ld(c,i,u) st() LO(c,i,u) ENV()"]
  N2789306708368 --> N2789306708240
  N2789306708240["ld(u) st() LO(c,i) ENV()"]
  N2789306708240 --> N2789306708560
  N2789306708560["ld() st(v) LO(c,i,v) ENV(v)"]
  N2789306708560 --> N2789306708944
  N2789306708944["ld(v) st() LO(c,i) ENV(v)"]
  N2789306708944 --> N2789306709072
  N2789306709072["ld(c) st() LO(i) ENV(v)"]
  N2789306709072 --> N2789306708816
  N2789306708816["ld(i) st() LO() ENV(v)"]
```
anon-1
```mermaid
graph TB
  N2789306706960["ld(c,g,i) st() LO(c,g,i) ENV()"]
  N2789306706960 --> N2789306707344
  N2789306707344["ld(g) st() LO(c,i) ENV()"]
  N2789306707344 --> N2789306707920
  N2789306707920["ld() st(u) LO(c,i,u) ENV(u)"]
  N2789306707920 --> N2789306708304
  N2789306708304["ld(c,i,u) st() LO() ENV(u)"]
```
p
```mermaid
graph TB
  N2789306630736["ld(sum) st(g) LO(g,sum) ENV(g)"]
  N2789306630736 --> N2789306631312
  N2789306631312["ld() st(i) LO(g,i,sum) ENV(g,i)"]
  N2789306631312 --> N2789306632144
  N2789306632144["ld(g,i) st() LO(g,i,sum) ENV(g,i)"]
  N2789306632144 --> N2789306633744
  N2789306633744["ld() st(h) LO(g,h,i,sum) ENV(g,h,i)"]
  N2789306633744 --> N2789306633872
  N2789306633872["ld(h) st() LO(g,i,sum) ENV(g,h,i)"]
  N2789306633872 --> N2789306704528
  N2789306704528["ld(sum) st() LO(g,i) ENV(g,h,i)"]
  N2789306704528 --> N2789306707088
  N2789306707088["ld() st(c) LO(c,g,i) ENV(c,g,h,i)"]
  N2789306707088 --> N2789306705552
  N2789306705552["ld(c,g,i) st() LO() ENV(c,g,h,i)"]
  N2789306705552 --> N2789306707408
  N2789306707408["ld() st(g) LO(g) ENV(c,g,h,i)"]
  N2789306707408 --> N2789306711632
  N2789306711632["ld(g) st() LO() ENV(c,g,h,i)"]
```
## Variable Collision Graph
```mermaid
graph TB
  g --- h
  g --- sum
  g --- i
  i --- v
  i --- sum
  i --- u
  c --- v
  c --- g
  c --- u
  c --- i
  h --- sum
  h --- i
```
