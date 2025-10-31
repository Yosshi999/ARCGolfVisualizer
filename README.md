# NeurIPS 2025 - Google Code Golf Championship
by Theoretical Syntax Golfers

# Setup
* Kaggleから問題をダウンロードし、jsonを`problems`配下にコピー
* `pip install -r requirements.txt`
* `flask run` でwebサーバー起動

# Writeup
WIP.

## Visualizer
Flask + Jinja2.

<img width="1859" height="893" alt="visualizer" src="https://github.com/user-attachments/assets/52cf2320-ea28-45fb-ab15-a37a75b54bfb" />

<img width="1324" height="923" alt="explorer" src="https://github.com/user-attachments/assets/cb6b34b0-6680-4f9b-a6ff-3e08a51f1cc4" />

<img width="1599" height="897" alt="problem viewer" src="https://github.com/user-attachments/assets/f7c52740-835d-40fd-ae37-80d99347155e" />


## LLM usage
A little. Claude generated summaries of problems based on [ARC dataset](https://github.com/google/ARC-GEN).

## ZLIB
https://github.com/google/zopfli

### Compress
```py
compressed_str = zopfli.zlib.compress(raw_str)[2:-4]
```

### Decompress
```py
#coding:L1
import zlib
exec(zlib.decompress(bytes(" ... ","L1"),-8))
```

### Effectiveness
<img width="574" height="455" alt="compression effectiveness" src="https://github.com/user-attachments/assets/5b0aa804-f08b-4c03-b461-3f154235bb26" />

It works well for >240B

### ZLIB-friendly techniques
* Do not use renaming like `R=range`

同文字列の繰り返し削減は、1文字変数で置換するよりも zlib に任せる方がほとんどのケースで強い。
（雑な解釈だが）zlib が採用する LZ77 アルゴリズムは、繰り返しパターンの置換による圧縮を行う方式である。繰り返し部分が R と短くなる代わりに、R=range; 部分のオーバーヘッドが生まれるので、zlib の圧縮が効きづらくなっているのではないか。
ものすごく雑な一般化をすると、「覗き穴最適化レベルのコード短縮は、zlib のサイズ短縮につながらない」「zlib のサイズ短縮には、アルゴリズムレベルの短縮が必要」と言えそう。

* Rename variables

変数名を適当にリネームすると、圧縮後のサイズが10B〜20B縮むことがザラにある。
縮む条件は要調査。
ちなみに、焼きなましで雑に変数名最適化をすると、ほとんどの変数名が小文字になる。コードの他の部分に登場するアルファベットを使うのが強いのだろうか？

## ZLIB Optimizer
Renaming variables gains ~400 pts.

`python sa_compress_tasks.py`

### Initial Guess
https://github.com/Yosshi999/ARCGolfVisualizer/blob/master/zlib_optimizer/optimizer.py#L92

It takes much computational cost for validation.
We generate initial guesses by using Optuna (or QUBO solver in early phase) with the constraint provided by the variable liveness analysis.

### Annealing
https://github.com/Yosshi999/ARCGolfVisualizer/blob/master/zlib_optimizer/zip_src.py#L137

Find the best variable renaming with only validating 10 cases.

## Golf Techniques
### Flatten
```py
sum(g,[])
```

### UnFlatten
```py
[*zip(*[iter(G)]*W)]
```

### Transpose
```py
[*map(list,zip(*g))]
[*zip(*g)]    # 注：内側がtupleになる
zip(*g)       # 注：not subscriptable
```

### Rotate left
```py
[*map(list,zip(*g))][::-1]
[*zip(*g)][::-1]    # 注：内側がtupleになる
```

### Rotate right
```py
[*map(list,zip(*g[::-1]))]
[*zip(*g[::-1])]    # 注：内側がtupleになる
zip(*g[::-1])       # 注：not subscriptable
```

### Clone
```py
[[*v]for v in g]
[v[:]for v in g]
[*map(list,g)]
```

### ColumnSum
```py
[sum(v)for v in zip(*g)]
```

### Dual axis
```py
def f(g):
 ... transpose and process ...
 return something
p=lambda g:f(f(g))
```

### Temporary array
```py
# ex. task 009
f=lambda g:[*map(list,zip(*[[max(
[k*10 if k<10 and v[i%3::3].index(k)<i//3<(len(v)//3-v[-(i%3+1)::-3].index(k))else v[i] for k in set(v[i%3::3])])for i in range(len(v))]for v in g]))];
p=lambda g:[[i//10 if i>9 else i for i in v] for v in f(f(g))]
```

### zeros_like
```py
[[0]*len(u)for u in g]
```

### Outer Rectangle
```py
E=enumerate
m=n=30;M=N=0
for i,v in E(g):
 for j,x in E(v):
  if ...:
   m=min(m,i);n=min(n,j);M=max(M,i);N=max(N,j)

# 条件を1行で書けるならこれが短い
E=enumerate
(u,*_,d),(l,*_,r)=map(sorted,zip(*[(i,j)for i,v in E(g)for j,w in E(v)if ...]))

# 長方形の4隅検出みたいに、最左上点と最右下点が存在するならこれでOK
E=enumerate
(u,l),*_,(d,r)=zip(*[(i,j)for i,v in E(g)for j,w in E(v)if ...])
```

### Count color
```py
最多の色c
s=sum(g,[]);c=max(s,key=s.count)

出現数でソート
# sorted単体では[1,1,1,1,2,2,2,2,2,2,...]となる
# dictは追加順が保持されるのでuniqに使える
s=sum(g,[]);c=[*{k:0for k in sorted(s,key=s.count)}]
```

### Remove parentheses
```py
(x+1)%w
-~x%w

(x-1)%w
~-x%w
```

### Append
```py
X.append(0)
X+=[0]

X.add(0)
X|={0}
```

### Remove map/zip
sortedはlistを返すので外さなくて良い
参考：https://peps.python.org/pep-3132/

```py
# listに直す
[*hoge]

# setに直す
{*hoge}

# tupleに直す
(*hoge,)

# 左辺をコンマ区切りにして受ける手もある
a,b=map(...)

# 長さ1のset sから値を取り出す
a,=[*s]
# 0とその他一色からなる行から色を得る
a,=[*{*v}-{0}]
_,a={*v}      # 全て非負の場合

# 右辺の個数が可変の場合
a,b,*c=(1,2,3,4) # -> a=1,b=2,c=[3,4]
a,*b,c=(1,2,3,4) # -> a=1,b=[2,3],c=4
*a,b,c=(1,2,3,4) # -> a=[1,2],b=3,c=4

# こういう書き方もできる
*w,=g
for*w,in zip(*g): ...    # memo: listのlistになってくれて、うれしい
(i,j),*_=((y,x)for ...)  # tupleへの代入と組み合わせることもできる
```

### Repeat
```py
# インデックスが必要な場合
for i in range(3)
for i in[0,1,2]

# 値だけ使う場合
for i in range(len(v))
for x in v

# 繰り返し回数だけ指定したい場合
for i in range(N) 
for _ in'.'*N

# インデックスと値両方使う場合、下の方が短いことも
for i in range(len(v))
for i,x in enumerate(v)

# range(len)を縦横にやる系は以下が良さそう
e=enumerate
for i,v in e(g):
 for j,w in e(v):

# 2重ループを1重にしてdiv/modで取り出す方が短いことがある
for y in range(H):
 for x in range(W):
  g[y][x]...
for z in range(H*W):g[y:=z//W][x:=z%W]... 

# execを使った方が短くなることがある
for _ in"..":
 ...

exec("""... """*2)
```

### If branch
```py
X if COND else Y
(Y,X)[COND]      # 注：短絡評価されなくなる

X if X else Y
X or Y

X if X and Y else 0
Y and X
X*(Y>0)
```

一度文字列にしてから置換すると短いこともある。`str.replace`, `str.translate`, `re.sub`, `re.subn` などが使用可能
```py
p=lambda g:eval(f'{g}'.replace(...))
```

### Slice
```py
# 例：task053
g[2:]+g[:2]
(g+g)[2:5]
```

### Variable in Lambda function
```py
# 基本的にはこう
p=lambda g:[[... foo:= ...]]

# 上で無理な場合はこう (※要検証)
p=lambda g:(foo:=..., ...foo...)[1]
```

### DFS
```py
R=range
def D(g,y,x):
 if len(g[0])>x>-1<y<len(g)>0<(c:=g[y][x]):g[y][x]-=99;return sum((D(g,y+a%3-1,x+a//3-1)for a in R(9)),[(y,x,c)])
 return[]
 
# p(g)の中に入れる、G=sum(g,[])が存在する前提
# x方向左右に行ってもよいかの検査はきびしめに検査しているので、縮むことはある ([-1,-W,-~z%W>0,W][z%W<1:] の部分) 
D=lambda z:L>z>=0<(c:=G[z])and sum((D(z+a)for a in[-1,-W,-~z%W>0,W][z%W<1:G.__setitem__(z,c-99)]),[(z,c)])or[]
```

### BFS
```py
Q=[(s,t)]
for i,j in Q:
 if g[i][j]>0:g[i][j]-=99;Q+=(i,~-j%w),(~-i%h,j),(-~i%h,j),(i,-~j%w) # 上下左右をキューに追加
```

### flip

* 線分の中央の取り方は、色のついているindexのリストをJとして`J=(J[(len(J)-1)//2]+J[len(J)//2])/2`
* 中央がグリッドの隙間に載っているときは0.5の端数がつく
* `g[i][j]`に対して、対象軸の反対側の位置は `g[i][j]=g[i][int(J+J-j)]`
