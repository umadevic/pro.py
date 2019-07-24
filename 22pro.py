#a
value=int(input())
arr=list(map(int,input().split()))
arr.sort(reverse=True)
#print(arr)
sum=0
sum1=0
res1=[]
for i in range(0,value,2):
    sum=sum+arr[i]
for j in range(1,value,2):
    sum1=sum1+arr[j]
res1.append([sum,sum1])
#print(res1)
for i in res1:
    print(i[0] if i[0]>i[1] else i[1])
