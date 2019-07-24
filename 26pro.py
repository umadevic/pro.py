#a
t2t=int(input())
sos1=list(map(int,input().split()))
u=[]
n1=1
for i in sos1:
  if i not in u:
    u.append(i)
for i in range(0,len(u)-1):
  if u[i]<u[i+1]:
    n1+=1
print(n1)
