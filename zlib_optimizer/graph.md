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
  N2369783710736["ld() st() LO() ENV()"]
  N2369783710736 --> N2369783710096
  N2369783710096["ld() st(p) LO() ENV()"]
```
anon-0
```mermaid
graph TB
  N2369783711760["ld(g,i) st() LO(g,i) ENV()"]
  N2369783711760 --> N2369783715280
  N2369783715280["ld(g) st() LO(i) ENV()"]
  N2369783715280 --> N2369783717392
  N2369783717392["ld() st(u) LO(i,u) ENV(u)"]
  N2369783717392 --> N2369783717264
  N2369783717264["ld(u) st() LO(i) ENV(u)"]
  N2369783717264 --> N2369783712976
  N2369783712976["ld() st(v) LO(i,v) ENV(u,v)"]
  N2369783712976 --> N2369783715664
  N2369783715664["ld(v) st() LO(i) ENV(u,v)"]
  N2369783715664 --> N2369783716944
  N2369783716944["ld(i) st() LO() ENV(u,v)"]
```
anon-2
```mermaid
graph TB
  N2369783772432["ld(c,i,u) st() LO(c,i,u) ENV()"]
  N2369783772432 --> N2369783772304
  N2369783772304["ld(u) st() LO(c,i) ENV()"]
  N2369783772304 --> N2369783772624
  N2369783772624["ld() st(v) LO(c,i,v) ENV(v)"]
  N2369783772624 --> N2369783773008
  N2369783773008["ld(v) st() LO(c,i) ENV(v)"]
  N2369783773008 --> N2369783773136
  N2369783773136["ld(c) st() LO(i) ENV(v)"]
  N2369783773136 --> N2369783772880
  N2369783772880["ld(i) st() LO() ENV(v)"]
```
anon-1
```mermaid
graph TB
  N2369783771792["ld(c,g,i) st() LO(c,g,i) ENV()"]
  N2369783771792 --> N2369783771664
  N2369783771664["ld(g) st() LO(c,i) ENV()"]
  N2369783771664 --> N2369783771984
  N2369783771984["ld() st(u) LO(c,i,u) ENV(u)"]
  N2369783771984 --> N2369783772368
  N2369783772368["ld(c,i,u) st() LO() ENV(u)"]
```
p
```mermaid
graph TB
  N2369783714192["ld(sum) st(g) LO(g,sum) ENV(g)"]
  N2369783714192 --> N2369783712784
  N2369783712784["ld() st(i) LO(g,i,sum) ENV(g,i)"]
  N2369783712784 --> N2369777916624
  N2369777916624["ld(g,i) st() LO(g,i,sum) ENV(g,i)"]
  N2369777916624 --> N2369783715344
  N2369783715344["ld() st(h) LO(g,h,i,sum) ENV(g,h,i)"]
  N2369783715344 --> N2369783715088
  N2369783715088["ld(h) st() LO(g,i,sum) ENV(g,h,i)"]
  N2369783715088 --> N2369783771280
  N2369783771280["ld(sum) st() LO(g,i) ENV(g,h,i)"]
  N2369783771280 --> N2369783765264
  N2369783765264["ld() st(c) LO(c,g,i) ENV(c,g,h,i)"]
  N2369783765264 --> N2369783771728
  N2369783771728["ld(c,g,i) st() LO() ENV(c,g,h,i)"]
  N2369783771728 --> N2369783769424
  N2369783769424["ld() st(g) LO(g) ENV(c,g,h,i)"]
  N2369783769424 --> N2369783774544
  N2369783774544["ld(g) st() LO() ENV(c,g,h,i)"]
```
## Variable Collision Graph
```mermaid
graph TB
  i --- u
  i --- v
  g --- i
  g --- h
  c --- i
  c --- u
  c --- v
  c --- g
  h --- i
```
