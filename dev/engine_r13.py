import json,os,sys,urllib.request as u
V=[0,100,320,330,500,1000,0]
KN=[-33,-31,-18,-14,14,18,31,33]
KG=[-17,-16,-15,-1,1,15,16,17]
BD=[-17,-15,15,17]
RD=[-16,-1,1,16]
AD=BD+RD
def _y(s,ds):
 return [[s+d*k for k in range(1,8) if not (s+d*k)&0x88] for d in ds]
RB=[_y(s,BD) for s in range(128)];RR=[_y(s,RD) for s in range(128)]
NM,GM=[[[s+d for d in D if not (s+d)&0x88] for s in range(128)] for D in (KN,KG)]
RQ=[RB[s]+RR[s] for s in range(128)]
MV=[0,0,[[[t] for t in NM[s]] for s in range(128)],RB,RR,RQ,[[[t] for t in GM[s]] for s in range(128)]]
PP=[0,5,10,20,35,55,85,120]
TP='SSSS~~~~]]gqXX]lSSSgXNISX]]?SSSS'
TN='!+55+?SS5S]b5Xbg5Sbg5X]b+?SX!+55'
TB='?IIIISSSISX]IXX]IS]]I]]]IXSS?III'
TR='SSSSX]]]NSSSNSSSNSSSNSSSNSSSSSSX'
TQ='?IINISSSISXXNSXXSSXXISXXISXS?IIN'
TK='5++!5++!5++!5++!?55+I???ggSSgq]S'
TE='!+5?5?IS5Igq5Iq{5Iq{5Igq55SS!555'
def _m(T):
 w=[0]*128;b=[0]*128;t=[ord(c)-83 for c in T]
 for R in range(8):
  for f in range(8):
   g=f if f<4 else 7-f
   w[R*16+f]=t[(7-R)*4+g];b[R*16+f]=t[R*4+g]
 return w,b
PT=[None]*13
for _i,_T in enumerate((TP,TN,TB,TR,TQ)):
 _w,_b=_m(_T);PT[7+_i]=_w;PT[5-_i]=_b
KA,KB=_m(TK);KC,KD=_m(TE)
ZB=[[hash((i,s)) for s in range(128)] for i in range(12)]
ZS=hash((12,0));ZC=[hash((13,i)) for i in range(16)];ZE=[hash((14,i)) for i in range(8)]
B=[0]*128;S=1;C=0;E=-1;K=[4,116];O=set();T=[];P=-1;H=[];X={};L=[[-1,-1] for _ in range(256)];Y=[[0]*128 for _ in range(7)];D=0;N=0
LIM=60000
class AB(Exception):pass
def f(F):
 global B,S,C,E,K,O,T,P,H,N
 B=[0]*128;O=set();K=[-1,-1];T=[];P=-1;H=[];N=0
 w=F.split();r=7
 for row in w[0].split('/'):
  c=0
  for ch in row:
   if ch.isdigit():c+=int(ch)
   else:
    q=r*16+c;p='PNBRQK'.index(ch.upper())+1
    if ch.islower():p=-p
    B[q]=p;O.add(q)
    if abs(p)==6:K[0 if p>0 else 1]=q
    c+=1
  r-=1
 S=1 if w[1]=='w' else -1
 C=0
 if len(w)>2:
  for ch in w[2]:C|={'K':1,'Q':2,'k':4,'q':8}.get(ch,0)
 E=-1
 if len(w)>3 and w[3]!='-':E=(int(w[3][1])-1)*16+ord(w[3][0])-97
def k():
 z=ZS if S<0 else 0
 for s in O:z^=ZB[B[s]-1 if B[s]>0 else -B[s]+5][s]
 z^=ZC[C]
 if E>=0:z^=ZE[E&7]
 return z
def a(s,c):
 for t in NM[s]:
  if B[t]==(2 if c>0 else -2):return 1
 for t in GM[s]:
  if B[t]==(6 if c>0 else -6):return 1
 for q in RB[s]:
  for t in q:
   x=B[t]
   if x:
    if (x>0)==(c>0) and abs(x) in (3,5):return 1
    break
 for q in RR[s]:
  for t in q:
   x=B[t]
   if x:
    if (x>0)==(c>0) and abs(x) in (4,5):return 1
    break
 d=-16 if c>0 else 16
 for t in (s+d-1,s+d+1):
  if not t&0x88 and B[t]==(1 if c>0 else -1):return 1
 return 0
def m(c):
 n=0
 for s in O:
  p=B[s]
  if not p or (p>0)!=(c>0):continue
  x=abs(p)
  if x==2:
   for t in NM[s]:
    y=B[t]
    if not y or (y>0)!=(c>0):n+=1
  elif 3<=x<=5:
   for q in (RB[s] if x==3 else RR[s] if x==4 else RQ[s]):
    for t in q:
     y=B[t]
     if y:
      if (y>0)!=(c>0):n+=1
      break
     n+=1
 return n
def j(k,c):
 n=0
 for d in KG:
  t=k+d
  if not t&0x88 and B[t]==c:n+=1
 return n*7
def e():
 s=0;ph=0;wp=[];bp=[];wr=[];br=[];wb=0;bb=0
 for q in O:
  p=B[q];x=abs(p)
  if x==6:continue
  if x==1:(wp if p>0 else bp).append(q)
  elif x==3:
   if p>0:wb+=1
   else:bb+=1
  elif x==4:(wr if p>0 else br).append(q)
  ph+=1 if x in (2,3) else 2 if x==4 else 4 if x==5 else 0
  s+=(V[x]+PT[p+6][q])*(1 if p>0 else -1)
 if wb>=2:s+=30
 if bb>=2:s-=30
 wf=[0]*8;bf=[0]*8;bh=[-1]*8;wl=[8]*8
 for q in wp:
  g=q&7;wf[g]+=1
  if (q>>4)<wl[g]:wl[g]=q>>4
 for q in bp:
  g=q&7;bf[g]+=1
  if (q>>4)>bh[g]:bh[g]=q>>4
 for ps,sg in ((wp,1),(bp,-1)):
  for q in ps:
   r=q>>4;g=q&7
   if sg>0:
    if max(bh[g-1] if g>0 else -1,bh[g],bh[g+1] if g<7 else -1)<=r:s+=PP[r]
   elif min(wl[g-1] if g>0 else 8,wl[g],wl[g+1] if g<7 else 8)>=r:s-=PP[7-r]
 for rs,sg in ((wr,1),(br,-1)):
  for q in rs:
   g=q&7
   if wf[g]+bf[g]==0:s+=16*sg
 s+=(KA[K[0]]*ph+KC[K[0]]*(24-ph))//24-((KB[K[1]]*ph+KD[K[1]]*(24-ph))//24)
 s+=j(K[0],1)-j(K[1],-1)
 s+=(m(1)-m(-1))*2
 return (s+8*S)*S
def mk(m):
 global S,C,E,P,N
 f=m&127;t=(m>>7)&127;pr=m>>14;p=B[f];cap=B[t];cs=-1;rf=-1;rt=-1;oc=C;oe=E;op=P;on=N
 if abs(p)==1 and t==E and cap==0 and (f&7)!=(t&7):
  cs=t-16 if p>0 else t+16;cap=B[cs];B[cs]=0;O.discard(cs)
 B[f]=0;O.discard(f);np=(pr if p>0 else -pr) if pr else p;B[t]=np;O.add(t)
 if abs(p)==6:
  K[0 if p>0 else 1]=t
  if t-f==2:rf,rt=f+3,f+1
  elif f-t==2:rf,rt=f-4,f-1
  C&=~(3 if p>0 else 12)
  if rf>=0:
   rp=B[rf];B[rf]=0;B[rt]=rp;O.discard(rf);O.add(rt)
 for q,bb in ((0,2),(7,1),(112,8),(119,4)):
  if (f==q and abs(p)==4) or (t==q and cap and abs(cap)==4):C&=~bb
 E=-1
 if abs(p)==1 and abs(t-f)==32:E=(f+t)//2
 S=-S;P=m;N=0
 T.append((m,cap,cs,oc,oe,rf,rt,op,on))
def uk():
 global S,C,E,P,N
 m,cap,cs,oc,oe,rf,rt,op,on=T.pop()
 f=m&127;t=(m>>7)&127;pr=m>>14;p=B[t]
 if rf>=0:
  rp=B[rt];B[rt]=0;B[rf]=rp;O.discard(rt);O.add(rf)
 B[t]=0;O.discard(t)
 if cs>=0:B[cs]=cap;O.add(cs)
 elif cap:B[t]=cap;O.add(t)
 B[f]=(1 if p>0 else -1) if pr else p;O.add(f)
 if abs(p)==6:K[0 if p>0 else 1]=f
 C=oc;E=oe;S=-S;P=op;N=on
def nl():
 global S,E,N
 T.append((-1,0,-1,C,E,-1,-1,P,N));S=-S;E=-1;N=1
def ul():
 global S,E,N
 m,cap,cs,oc,oe,rf,rt,op,on=T.pop();S=-S;E=oe;N=on
def g(cp):
 ms=[];Bl=B
 mv=S
 for sq in O:
  p=Bl[sq]
  if not p or (p>0)!=(S>0):continue
  x=abs(p);r=sq>>4
  if x==1:
   dr=16 if p>0 else -16
   prm=(r==6 and p>0) or (r==1 and p<0)
   for dt in (dr,dr-1,dr+1):
    t=sq+dt
    if t&0x88:continue
    pu=dt==dr
    if pu:
     if Bl[t] or cp:continue
    elif Bl[t]:
     if (Bl[t]>0)==(p>0):continue
    elif t!=E:continue
    if prm:
     for pr in (5,4,3,2):ms.append(sq|(t<<7)|(pr<<14))
    else:
     ms.append(sq|(t<<7))
     if pu and ((p>0 and r==1) or (p<0 and r==6)):
      t2=sq+dr*2
      if not Bl[t2]:ms.append(sq|(t2<<7))
  else:
   for q in MV[x][sq]:
    for t in q:
     y=Bl[t]
     if y:
      if (y>0)!=(p>0):ms.append(sq|(t<<7))
      break
     if not cp:ms.append(sq|(t<<7))
   if x==6 and not cp:
    for c,ks,es,ss,xq in (((1,4,6,5,-1),(2,4,2,3,1)) if p>0 else ((4,116,118,117,-1),(8,116,114,115,113))):
     if C&c and not Bl[es] and not Bl[ss] and (xq<0 or not Bl[xq]) and not a(ks,1 if ks>100 else -1) and not a(ss,1 if ks>100 else -1) and not a(es,1 if ks>100 else -1):ms.append(ks|(es<<7))
 out=[]
 for m in ms:
  mk(m)
  if not a(K[0] if mv>0 else K[1],S):out.append(m)
  uk()
 return out
def o(m,tm,ply):
 f=m&127;t=(m>>7)&127;pr=m>>14
 cap=B[t] or (abs(B[f])==1 and t==E)
 v=0
 if cap:v=10*V[abs(B[t])]-V[abs(B[f])]//10
 if pr:v+=900+100*pr
 if m==tm:v+=1000000
 if m==L[ply][0]:v+=900000
 elif m==L[ply][1]:v+=800000
 v+=Y[abs(B[f])][t]
 return v
def q(al,be,ply):
 global D
 D+=1
 if D>=LIM:raise AB
 z=k()
 if z in H:return 0
 st=e()
 if st>=be:return st
 inc=a(K[0] if S>0 else K[1],-S)
 if inc:
  ms=g(0)
  if not ms:return -100000+ply
 else:
  ms=g(1)
  if not ms:return st
 ms.sort(key=lambda m:o(m,-1,ply),reverse=True)
 bv=st
 for m in ms:
  mk(m)
  s=-q(-be,-al,ply+1)
  uk()
  if s>bv:bv=s
  if s>al:al=s
  if al>=be:break
 return bv
def r(d,al,be,ply):
 global D
 D+=1
 if D>=LIM:raise AB
 z=k()
 if z in H:return 0
 v=X.get(z)
 ttm=-1
 if v:
  ed,ef,es,em=v
  if ed>=d:
   es2=es-ply if es>90000 else es+ply if es<-90000 else es
   if ef==0:return es2
   if ef==1 and es2>=be:return es2
   if ef==2 and es2<=al:return es2
  ttm=em
 inc=a(K[0] if S>0 else K[1],-S)
 if d<=0:return q(al,be,ply)
 H.append(z)
 try:
  if not inc and d>=3 and not N:
   st=e()
   if st>=be and any(abs(p:=B[sq]) not in (1,6) and (p>0)==(S>0) for sq in O):
    R=3 if d>6 else 2
    nl();s=-r(d-1-R,-be,-be+1,ply+1);ul()
    if s>=be:return be
  ms=g(0)
  if not ms:return -100000+ply if inc else 0
  ms.sort(key=lambda m:o(m,ttm,ply),reverse=True)
  bv=-1000000;bm=-1;bmc=0;a0=al
  for i,m in enumerate(ms):
   f=m&127;t=(m>>7)&127;pr=m>>14
   cap=B[t] or (abs(B[f])==1 and t==E)
   mk(m)
   if i and d>=3 and not cap and not pr and not inc and m not in L[ply]:
    s=-r(d-2-(d>=6 and i>6),-al-1,-al,ply+1)
    if s>al:s=-r(d-1,-be,-al,ply+1)
   else:
    s=-r(d-1,-be if i==0 else -al-1,-al,ply+1)
    if i and s>al:s=-r(d-1,-be,-al,ply+1)
   uk()
   if s>bv:bv=s;bm=m;bmc=cap
   if s>al:al=s
   if al>=be:break
  if al>=be and bm>=0 and not bmc and not (bm>>14):
   if L[ply][0]!=bm:L[ply][1]=L[ply][0];L[ply][0]=bm
   Y[abs(B[bm&127])][(bm>>7)&127]=min(Y[abs(B[bm&127])][(bm>>7)&127]+d*d,1000000)
  fl=2 if bv<=a0 else 1 if bv>=be else 0
  sv=bv+ply if bv>90000 else bv-ply if bv<-90000 else bv
  X[z]=(d,fl,sv,bm)
  return bv
 finally:
  H.pop()
def t(d,al,be):
 ms=g(0)
 if not ms:return -1,0
 z=k();v=X.get(z);ttm=v[3] if v else -1
 ms.sort(key=lambda m:o(m,ttm,0),reverse=True)
 bv=-1000000;bm=ms[0]
 for i,m in enumerate(ms):
  mk(m)
  if i==0:s=-r(d-1,-be,-al,1)
  else:
   s=-r(d-1,-al-1,-al,1)
   if al<s<be:s=-r(d-1,-be,-al,1)
  uk()
  if s>bv:bv=s;bm=m
  if s>al:al=s
  if al>=be:break
 X[z]=(d,0,bv,bm)
 return bm,bv
def h():
 global D,L,Y,H
 D=0;H=[];L=[[-1,-1] for _ in range(256)];Y=[[0]*128 for _ in range(7)]
 ms=g(0)
 if not ms:return -1
 if len(ms)==1:return ms[0]
 bm=ms[0];bs=0;sd=len(T)
 for d in range(1,65):
  try:
   nb,ns=t(d,-1000000,1000000)
   bm,bs=nb,ns
  except AB:
   break
 while len(T)>sd:
  if T[-1][0]==-1:ul()
  else:uk()
 return bm
def p(path,bd):
 rq=u.Request(U+path,data=json.dumps(bd).encode(),headers={"content-type":"application/json"})
 try:
  with u.urlopen(rq) as rr:return json.load(rr)
 except Exception as ex:sys.exit(str(ex))
if __name__=="__main__":
 U=os.environ.get("MAKEFUN_ENV_URL") or sys.exit("MAKEFUN_ENV_URL is not set")
 while 1:
  gg=p("/game",{})
  if gg["status"]=="done":break
  while gg["status"]=="your_move":
   f(gg["fen"])
   mm=h()
   if mm<0:sys.exit("no legal move")
   ff=mm&127;tt=(mm>>7)&127;pr=mm>>14
   gg=p("/move",{"game":gg["game"],"move":"abcdefgh"[ff&7]+str((ff>>4)+1)+"abcdefgh"[tt&7]+str((tt>>4)+1)+("nbrq"[pr-2] if pr else "")})
