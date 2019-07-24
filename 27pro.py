#a
s,f=map(int,input().split())

m=list(map(int,input().split()))

v=list(map(int,input().split()))

t=[]

c=0

for i in range(s):

    x=v[i]/m[i]

    t.append(x)

while f>=0 and len(t)>0:

    mindex=t.index(max(t))

    if f>=m[mindex]:

        c=c+v[mindex]

        f=f-m[mindex]

    m.pop(mindex)

    v.pop(mindex)

    t.pop(mindex)

print(c)
