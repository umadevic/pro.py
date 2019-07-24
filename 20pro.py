s,u=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort(reverse=True)
y=0
total=u
for i in arr:
    if total>=i:
        rem=int(total/i)
        y+=rem
        total=total - (i*rem)
    if total==0:
        break
if total==0:
    print(y)
else:
    print("it's not possible to sum up coins in such a way that they um upto",u)
